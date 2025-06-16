#!/bin/bash

# Update and install required packages
dnf update -y
dnf install -y python3 git mesa-libGL  # For OpenCV (libGL.so.1)

# Set up a Python virtual environment
python3 -m venv /home/ec2-user/pixenv
source /home/ec2-user/pixenv/bin/activate

# Clone the GitHub repo
cd /home/ec2-user
git clone https://github.com/mohdishaq786/Api-Pixelshowroom.git
cd Api-Pixelshowroom

# Install Python dependencies
/home/ec2-user/pixenv/bin/pip install --upgrade pip
/home/ec2-user/pixenv/bin/pip install -r requirements.txt

# Paths to SSL certificate and key (stored inside the repo)
CERT_PATH="/home/ec2-user/Api-Pixelshowroom/aws/certs/fullchain.pem"
KEY_PATH="/home/ec2-user/Api-Pixelshowroom/aws/certs/privkey.pem"

# Run the FastAPI app with HTTPS on port 443
nohup sudo /home/ec2-user/pixenv/bin/python -m uvicorn main:app \
    --host 0.0.0.0 \
    --port 443 \
    --ssl-certfile "$CERT_PATH" \
    --ssl-keyfile "$KEY_PATH" \
    > /home/ec2-user/server.log 2>&1 &
