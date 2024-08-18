# Use the official Python image as a base
FROM python:3.9-slim

# Set the working directory to /app
WORKDIR /app

# Copy the requirements file
COPY requirements.txt .

# Install the dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Copy the judge code
COPY judge.py .

# Make the judge code executable
RUN chmod +x judge.py

# Set the environment variable for the instance ID
ENV INSTANCE_ID=None

# Run the judge code when the container starts
CMD ["python", "-u", "judge.py"]

