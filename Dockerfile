FROM nikolaik/python-nodejs:latest

# Update system and install ffmpeg
RUN apt update && apt upgrade -y && apt install ffmpeg -y

# Set working directory
WORKDIR /app

# Copy project files
COPY . .

# Set permissions (optional, but safer to limit scope)
RUN chmod -R 755 /app

# Create virtual environment
RUN python3 -m venv /app/venv
ENV PATH="/app/venv/bin:$PATH"

# Upgrade pip and install dependencies
RUN pip install --upgrade pip
RUN pip install --no-cache-dir -r requirements.txt

# Start the bot
CMD ["python", "main.py"]
