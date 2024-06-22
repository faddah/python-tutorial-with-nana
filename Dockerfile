# Use the official Python 3.12.3 image.
FROM python:3.12.3

# Set the working directory inside the container
WORKDIR /usr/src/app

# Copy the requirements file into the container at /usr/src/app
COPY requirements.txt ./

# Install any dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Copy the local code to the container
COPY . .

# Command to run on container start
CMD ["python", "./main.py"]