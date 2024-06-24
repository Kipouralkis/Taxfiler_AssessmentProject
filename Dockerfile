# Specify the base image
FROM python:3.8-slim

# Working directory where the files will be copied and commands be executed
WORKDIR /app

# Copy files to dir
COPY . .

# Install requirements
RUN pip3 install --no-cache-dir -r requirements.txt

# Make port 5000 available to the world outside this container
EXPOSE 5000

# Define default environment variables
ENV FLASK_APP=app.py
ENV OPENAI_API_KEY ""
ENV FLASK_RUN_HOST=0.0.0.0
ENV FLASK_RUN_PORT=5000

# Default command arguments
CMD ["python3", "-m", "flask", "run", "--host=0.0.0.0"]