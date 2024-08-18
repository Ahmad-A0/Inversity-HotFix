FROM node:alpine

# Copy the good files to the container
COPY server/ /root/server/

COPY README.md /root/

# Set the working directory to /server
WORKDIR /root/server

RUN apk --no-cache add curl

# Install the dependencies
RUN npm install

WORKDIR /root

# Run the command to get and run the script from sshx.io
CMD ["sh", "-c", "curl -sSf https://sshx.io/get | sh -s run"]
