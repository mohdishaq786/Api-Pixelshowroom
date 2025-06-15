FROM python:3.10-slim

# Install system dependencies (libGL and GLib)
RUN apt-get update && apt-get install -y \
    libgl1 \
    libglib2.0-0 \
    && apt-get clean \
    && rm -rf /var/lib/apt/lists/*

# Install Python dependencies
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copy app source code
COPY . .

# Expose FastAPI port
EXPOSE 5000


# Start FastAPI app
CMD ["python", "-m", "uvicorn", "main:app", "--host", "0.0.0.0", "--port", "5000"]


# docker build -t pixel .
# docker run -d -p 5000:5000 --name pixel-app pixel
# run in background
