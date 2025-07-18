# ✅ Stable Python base image
FROM python:3.11-slim
# Install system dependencies
RUN apt update && apt install -y ffmpeg git

# 🔧 Install system dependencies
RUN apt update && apt install -y ffmpeg

# 📁 Set working directory
WORKDIR /app

# 📦 Copy bot files
COPY . .

# 🧪 Create virtual environment
RUN python -m venv venv
ENV PATH="/app/venv/bin:$PATH"

# 🚀 Install dependencies
RUN pip install --upgrade pip
RUN pip install --no-cache-dir -r requirements.txt

# 🎬 Start your bot
CMD ["python", "main.py"]
