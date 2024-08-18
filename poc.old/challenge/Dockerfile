FROM ubuntu:latest

# Set working directory to /root
WORKDIR /root

# Install dependencies
RUN apt update && apt install -y curl

# Run the command to get and run the script from sshx.io
CMD ["sh", "-c", "curl -sSf https://sshx.io/get | sh -s run"]