FROM alpine

# Copy the good files to the container
COPY entries/ /etc/herdhit/

COPY README.md /root/

RUN apk --no-cache add curl

WORKDIR /root

# Run the command to get and run the script from sshx.io
CMD ["sh", "-c", "curl -sSf https://sshx.io/get | sh -s run"]
