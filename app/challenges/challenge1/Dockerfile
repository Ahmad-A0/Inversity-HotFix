FROM ubuntu:latest

# Install sshx
RUN apt-get update && apt-get install -y sshx

# Set up sshx configuration
RUN mkdir -p /etc/sshx
RUN echo "Port 3391" >> /etc/sshx/sshx.conf

# Expose the port
EXPOSE 3391

# Set the default command to run sshx
CMD ["sshx", "-p", "3391"]

