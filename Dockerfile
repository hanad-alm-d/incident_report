# Use official Python image with version 3.10
FROM python:3.10-slim

# Set the working directory inside the container
WORKDIR /app

# Copy the requirements file and install the dependencies
COPY requirements.txt . 
RUN pip install --no-cache-dir -r requirements.txt

# Copy all application files into the container
COPY . .

# Expose the port that Flask will run on
EXPOSE 8000

# Start the Flask app using python run.py
CMD ["python", "run.py"]