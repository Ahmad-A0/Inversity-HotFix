from flask import Flask, request, jsonify
import docker
import os
import uuid

app = Flask(__name__)
client = docker.from_env()

CHALLENGE_DIR = os.path.join(os.path.dirname(__file__), 'challenges')

@app.route('/create_challenge', methods=['POST'])
def create_challenge():
    challenge_name = request.json.get('challenge_name')
    if not challenge_name:
        return jsonify({"error": "Challenge name is required"}), 400

    challenge_id = str(uuid.uuid4())
    
    try:
        # Build challenge image
        challenge_image, _ = client.images.build(
            path=os.path.join(CHALLENGE_DIR, challenge_name),
            tag=f"{challenge_name}:{challenge_id}"
        )

        # Build judge image
        judge_image, _ = client.images.build(
            path=os.path.join(CHALLENGE_DIR, f"{challenge_name}_judge"),
            tag=f"{challenge_name}_judge:{challenge_id}"
        )

        # Create networks
        internal_network = client.networks.create(
            f"internal_network_{challenge_id}",
            driver="bridge",
            internal=True
        )
        external_network = client.networks.create(f"external_network_{challenge_id}")

        # Run challenge container
        challenge_container = client.containers.run(
            f"{challenge_name}:{challenge_id}",
            detach=True,
            name=f"challenge_{challenge_id}",
            network=internal_network.name
        )

        # Run judge container
        judge_container = client.containers.run(
            f"{challenge_name}_judge:{challenge_id}",
            detach=True,
            name=f"judge_{challenge_id}",
            network=external_network.name,
            volumes={'/var/run/docker.sock': {'bind': '/var/run/docker.sock', 'mode': 'ro'}}
        )
        # Connect judge container to internal network
        internal_network.connect(judge_container, aliases=['judge'])

        return jsonify({
            "challenge_id": challenge_id,
            "challenge_container_id": challenge_container.id,
            "judge_container_id": judge_container.id
        }), 201

    except Exception as e:
        return jsonify({"error": str(e)}), 500

if __name__ == '__main__':
    app.run(debug=True)

