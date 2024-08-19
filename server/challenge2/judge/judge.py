import os
import docker
from time import sleep

GOOD_FILES_HASH = "4ed19489eb9922016d2a84f23cf063d6"
TESTS = [
    f"""sh -c 'if [ "$(md5sum /root/server/app.js | cut -d " " -f1)" = "{GOOD_FILES_HASH}" ]; then echo -n 1; else echo -n 0; fi'""",
    """sh -c 'if nc -z localhost 3000; then echo 1; else echo 0; fi'""",
]



def tests_passed(challenge_container, test_commands):
    for test_command in test_commands:
        output = challenge_container.exec_run(test_command)
        decoded = output.output.decode("utf-8")
        print("Running test: ", test_command)
        print(f"decoded: {decoded}")
        if decoded not in ["1", "1\n"]:
            print(f"Test failed: {test_command}")
            return False
        print(f"Test passed: {test_command}")
    return True


# -----

# Get the instance ID from the environment variable
instance_id = os.environ.get("INSTANCE_ID")

client = docker.from_env()

challenge_container_name = f"challenge2_challenge_{instance_id}"
provisioner_container_name = "inversity-provisioner-container"

tries = 0
while tries < 20:
    try:
        sleep(0.2)
        challenge_container = client.containers.get(challenge_container_name)
        provisioner_container = client.containers.get(provisioner_container_name)
        break
    except docker.errors.NotFound:
        print(
            f"Container {challenge_container_name} or {provisioner_container_name} not found"
        )
        tries += 1
        continue

while True:
    try:
        if tests_passed(challenge_container, TESTS):
            output = provisioner_container.exec_run(
                cmd=[
                    "/usr/local/bin/python",
                    "-c",
                    f'import requests; response = requests.post("http://localhost:8080/api/challenges/complete", json={{"challenge": "challenge2", "instance_id": "{instance_id}"}}); print(response.text)',
                ],
                stdout=True,
                stderr=True,
            )
            std_out = output.output.decode("utf-8")
            std_err = output.output.decode("utf-8")
            print(f"request output: {std_out}, {std_err}")
            break
        else:
            print(".", end="")
            sleep(1)
    except docker.errors.APIError as e:
        print(f"Error contacting server: {e}")
        sleep(1)