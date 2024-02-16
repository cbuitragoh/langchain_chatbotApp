# Use an official Python runtime as a parent image
FROM python:3.11

# Set the working directory in the container
WORKDIR /app

# Copy the requirements.txt
COPY ./main/requirements.txt /app/main/requirements.txt

# Install any needed dependencies specified in requirements.txt
RUN pip install --no-cache-dir --upgrade -r /app/main/requirements.txt

# Copy the current directory contents into the container at /app
COPY . /app

# Make port 80 available to the world outside this container
EXPOSE 80

# Run app.py when the container launches
CMD ["uvicorn", "main.chatbot:app", "--proxy-headers", "--host", "0.0.0.0", "--port", "80"]

