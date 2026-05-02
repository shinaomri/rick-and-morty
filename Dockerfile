# Start from an official Python image (slim = smaller size)
FROM python:3.11-slim

# Set the working directory inside the container
WORKDIR /app

# Copy requirements first (Docker caching trick - explained below)
COPY requirements.txt .

# Install dependencies
RUN pip install -r requirements.txt

# Copy the rest of our code
COPY . .

# Tell Docker our app listens on port 5000
EXPOSE 5000

# Command to run when container starts
CMD ["python", "app.py"]
