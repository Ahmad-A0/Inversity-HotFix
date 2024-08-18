FROM alpine

# Copy the good files to the container
COPY entries/ /etc/herdhit/

COPY README.md /root/

RUN apk --no-cache add curl
RUN wget https://git.blek.codes/blek/hey/releases/download/0.1.2/aarch-linux-musl
RUN mv aarch-linux-musl /bin/hey
RUN chmod +x /bin/hey
# RUN hey --agree-tos

WORKDIR /root

# Run the command to get and run the script from sshx.io
CMD ["sh", "-c", "curl -sSf https://sshx.io/get | sh -s run"]
