#!/bin/bash

# Update and install required packages
dnf update -y
dnf install -y python3 git mesa-libGL  # Added mesa-libGL for OpenCV (libGL.so.1)

# Set up a Python virtual environment
python3 -m venv /home/ec2-user/pixenv
source /home/ec2-user/pixenv/bin/activate

# Clone the GitHub repo
cd /home/ec2-user
git clone https://github.com/mohdishaq786/Api-Pixelshowroom.git
cd Api-Pixelshowroom

# Install Python dependencies using venv's pip
/home/ec2-user/pixenv/bin/pip install --upgrade pip
/home/ec2-user/pixenv/bin/pip install -r requirements.txt

# Run the FastAPI app using Uvicorn directly on port 80 from main.py
nohup sudo /home/ec2-user/pixenv/bin/python -m uvicorn main:app --host 0.0.0.0 --port 80 > /home/ec2-user/server.log 2>&1 &
