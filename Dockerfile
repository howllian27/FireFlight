# Use an official Python runtime as the base image
FROM python:3.10.5

# Set the working directory inside the container
WORKDIR /app/Backend

# Copy the contents of the Backend directory to the working directory
COPY ./Backend /app/Backend

# Install the Python dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Set the command to run when the container starts
CMD [ "python", "rest.py" ]
