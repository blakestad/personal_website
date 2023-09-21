# Use an official Python runtime as a parent image
FROM python:3.11.5-slim

# Set the working directory in the container
WORKDIR /app

# Copy the requirements.txt into the container at /app
COPY requirements.txt /app/

# Install any needed packages specified in requirements.txt
RUN pip install -r requirements.txt
RUN pip install gunicorn

# Copy the current directory contents into the container at /app
COPY . /app/

# Make port 8080 available to the world outside this container
EXPOSE 8080

# Run main.py when the container launches
CMD ["gunicorn", "-b", ":8080", "main:create_app()"]
