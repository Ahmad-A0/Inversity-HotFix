from flask import Flask, request, jsonify
from time import sleep
import re
import logging
import docker
import sys

app = Flask(__name__)

logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s",
    datefmt="%Y-%m-%d %H:%M:%S",
    stream=sys.stdout,
)

logger = logging.getLogger(__name__)

# Create a Docker client
client = docker.from_env()

# List of available challenges
challenges = {
    "challenge1": {
        "challenge_image": "challenge1/challenge",
        "judge_image": "challenge1/judge",
    },
    "challenge2": {
        "challenge_image": "challenge2/challenge",
        "judge_image": "challenge2/judge",
    },
    # Add more challenges here...
}


def find_link(output):
    match = re.search(r"Link: (.*)", output)
    if match:
        link = match.group(1)
        return link[8:-4]
    else:
        return None



# Route to select a challenge and provision containers
@app.route("/select", methods=["POST"])
def select_challenge():
    challenge_name = request.json.get("challenge")
    instance_id = request.json.get("instance_id")
    challenge = challenges.get(challenge_name)

    logger.info("Challenge %s selected with payload %s", challenge_name, challenge)

    if str(challenge):
        # Create a unique name for the challenge container
        challenge_container_name = f"{challenge_name}_challenge_{instance_id}"
        network = client.networks.create(
            name=f"{challenge_name}_network_{instance_id}", driver="bridge"
        )

        # Create a unique name for the judge container
        judge_container_name = f"{challenge_name}_judge_{instance_id}"

        # Create the challenge container
        challenge_container = client.containers.run(
            image=challenge["challenge_image"],
            detach=True,
            auto_remove=True,
            name=challenge_container_name,
            network=network.name,
        )

        judge_container = client.containers.run(
            image=challenge["judge_image"],
            detach=True,
            auto_remove=True,
            name=judge_container_name,
            network=network.name,
            # ports={'8080': 8081},  # Map port 8080 in the container to port 8081 on the host
            volumes={
                "/var/run/docker.sock": {"bind": "/var/run/docker.sock", "mode": "rw"}
            },
            environment=[f"INSTANCE_ID={instance_id}"],
        )

        # Get the output of the container
        output = challenge_container.logs(stdout=True, stderr=True).decode("utf-8")

        link = find_link(output)
        tries = 0
        while not link and tries < 20:
            sleep(0.25)
            output = challenge_container.logs(stdout=True, stderr=True).decode("utf-8")
            link = find_link(output)
            tries += 1

        return jsonify(
            {"link": link, "instance_id": instance_id, "challenge": challenge_name}
        )
    else:
        return f"Challenge {challenge_name} not found.", 404


# Route to complete a challenge
@app.route("/api/challenges/complete", methods=["POST"])
def complete_challenge():
    if request.remote_addr != "127.0.0.1":
        logger.error("Unauthorized access from %s", request.remote_addr)
        return jsonify({"success": False}), 401

    challenge_name = request.json.get("challenge")
    instance_id = request.json.get("instance_id")
    if challenge_name and instance_id:
        logger.info("Completing challenge %s with instance ID %s", challenge_name, instance_id)
        challenge_container_name = f"{challenge_name}_challenge_{instance_id}"
        judge_container_name = f"{challenge_name}_judge_{instance_id}"
        challenge_container = client.containers.get(challenge_container_name)
        judge_container = client.containers.get(judge_container_name)

        command = "for pts in /dev/pts/*; do echo -e '\\033[2J\\033[1;1H\\033[94m Congratulations, you have completed the challenge! \\033[0m\\033[1m Return to Inversity, and see where you place \\033[0m\\033[94m' > $pts; done"
        challenge_container.exec_run(cmd=["/bin/bash", "-c", command])

        # Cleanup
        challenge_container.stop()
        judge_container.stop()

        network = client.networks.get(f"{challenge_name}_network_{instance_id}")    
        network.remove()

        return jsonify({"success": True})
    else:
        logger.error("Missing challenge or instance ID")
        return jsonify({"success": False}), 400


# Run the web server
if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8080)
