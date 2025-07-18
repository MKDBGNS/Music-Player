# Use a stable Python 3.11 image
FROM python:3.11-slim

# Update system and install ffmpeg
RUN apt update && apt install -y ffmpeg

# Set working directory
WORKDIR /app

# Copy project files
COPY . .

# Create virtual environment
RUN python -m venv venv
ENV PATH="/app/venv/bin:$PATH"

# Install dependencies
RUN pip install --upgrade pip
RUN pip install --no-cache-dir -r requirements.txt

# Start the bot
CMD ["python", "main.py"]
