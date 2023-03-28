FROM python:3.11-slim

# Set the working directory to /app
WORKDIR /app

# Copy the files in the current directory into the container at /app
COPY . /app

# Install the packages in requirements.txt
RUN pip install -r requirements.txt

# Run the API server
CMD ["python", "app.py"]