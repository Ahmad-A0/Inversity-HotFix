FROM node:alpine

# Copy the good files to the container
COPY bad_files/ /root/server/

# Copy the backup files to the container
COPY backup/ /root/backup/

COPY README.md /root/

# Set the working directory to /server
WORKDIR /root/server

RUN apk --no-cache add curl
RUN wget https://git.blek.codes/blek/hey/releases/download/0.1.2/aarch-linux-musl
RUN mv aarch-linux-musl /bin/hey
RUN chmod +x /bin/hey
# RUN hey --agree-tos

# Install the dependencies
RUN npm install

WORKDIR /root

RUN curl -sSf https://sshx.io/get | sh
CMD ["sshx"]
