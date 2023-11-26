FROM python:3.12-bullseye

# Where we are in the container (basically equivalent to 'cd /app')
WORKDIR /app

# Set up python environment
# This is the first thing so that docker can cache it (changes later/below in the file will not invalidate this layer)
COPY requirements.txt /app
RUN pip install -r requirements.txt

# Copy code
# If copying a directory, the destination must end with a slash
COPY src/* /app/

# Copy model
COPY model.pkl /app

# Expose port 8000 from the container to the host
EXPOSE 8000

# Run the app (uvicorn is a production server)
CMD ["uvicorn", "api:app", "--host", "0.0.0.0", "--port", "8000"]

# The file structure inside the container is:
# /app
# ├── api.py
# ├── model.pkl
# ├── predict.py
# └── requirements.txt
