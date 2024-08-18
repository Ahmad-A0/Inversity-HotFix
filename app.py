from flask import Flask, request, jsonify
import logging
import docker
import sys

app = Flask(__name__)

logging.basicConfig(level=logging.INFO,
                    format='%(asctime)s - %(levelname)s - %(message)s',
                    datefmt='%Y-%m-%d %H:%M:%S',
                    stream=sys.stdout)

logger = logging.getLogger(__name__)

# Create a Docker client
client = docker.from_env()

# List of available challenges
challenges = {
    "challenge1": {
        "challenge_image": "challenge1/challenge",
        "judge_image": "challenge1/judge"
    },
    "challenge2": {
        "challenge_image": "challenge2/challenge",
        "judge_image": "challenge2/judge"
    },
    # Add more challenges here...
}

# Route to select a challenge and provision containers
@app.route('/select', methods=['POST'])
def select_challenge():
    challenge_name = request.json.get('challenge')
    challenge = challenges.get(challenge_name)

    logger.info('Challenge %s selected with payload %s', challenge_name, challenge)


    if challenge:
        # Create a unique name for the challenge container
        challenge_container_name = f"{challenge_name}_challenge_{request.form.get('instance_id')}"

        # Create a unique name for the judge container
        judge_container_name = f"{challenge_name}_judge_{request.json.get('instance_id')}"

        # Create the challenge container
        challenge_container = client.containers.run(
            image=challenge['challenge_image'],
            detach=True,
            auto_remove=True,
            name=challenge_container_name
        )

        # Create the judge container
        judge_container = client.containers.run(
            image=challenge['judge_image'],
            detach=True,
            name=judge_container_name,
            links={challenge_container_name: "challenge"},
            auto_remove=True,
            environment=[f"INSTANCE_ID={request.json.get('instance_id')}"],
            network_mode='host'  # Allow the judge container to access the host network
        )
        return f'Challenge {challenge_name} instance {request.form.get("instance_id")} selected and containers provisioned!'
    else:
        return f'Challenge {challenge_name} not found.', 404

# Route to complete a challenge
@app.route('/api/challenges/complete', methods=['POST'])
def complete_challenge():
    challenge_name = request.json.get('challenge')
    instance_id = request.json.get('instance_id')
    if challenge_name and instance_id:
        challenge_container_name = f"{challenge_name}_challenge_{instance_id}"
        judge_container_name = f"{challenge_name}_judge_{instance_id}"
        challenge_container = client.containers.get(challenge_container_name)
        judge_container = client.containers.get(judge_container_name)
        # Add code here to complete the challenge and return a success response
        return jsonify({'success': True})
    else:
        return jsonify({'success': False}), 400

# Run the web server
if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080)

