import os
import docker
import requests
from time import sleep

# Get the instance ID from the environment variable
instance_id = os.environ.get('INSTANCE_ID')

client = docker.from_env()

challenge_container_name = f"challenge1_challenge_{instance_id}"

try:
    challenge_container = client.containers.get(challenge_container_name)
except docker.errors.NotFound:
    print(f"Container {challenge_container_name} not found")
    exit(1)

while True:
    try:
        output = challenge_container.exec_run('test -f /root/test.txt && echo 1')
        decoded = output.output.decode("utf-8")

        if output:
            response = requests.post(f"http://0.0.0.0:8080/api/challenges/complete", json={'challenge': 'challenge1', 'instance_id': instance_id})
            if response.status_code == 200:
                break
            else:
                print(f"Error completing challenge: {response.text}")
                exit(1)
        else:
            sleep(5)
    except requests.exceptions.RequestException as e:
        print(f"Error contacting server: {e}")
        exit(1)

