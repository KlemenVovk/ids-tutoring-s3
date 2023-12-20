# Use the official Python 3.10 base image
FROM python:3.10-bookworm

# Set the working directory in the container
WORKDIR /app

# Copy the requirements file to the container
COPY requirements.txt .

# Install the dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Copy the main.py file to the container
COPY main.py .

# Run main.py every 30 seconds with a bash loop (there are many ways to do this - bash, cron, watch, etc.)
CMD ["bash", "-c", "while true; do python main.py; sleep 30; done"]
