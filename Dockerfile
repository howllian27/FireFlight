# Use an official Python runtime as the base image
FROM python:3.10.5

# Set the working directory inside the container
WORKDIR /Backend

# Set the command to run when the container starts
CMD [ "python", "rest.py" ]
