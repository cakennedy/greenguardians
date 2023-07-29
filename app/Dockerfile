FROM python:3.10-slim-buster

# Install Python dependencies.
COPY requirements.txt ./
RUN pip install --no-cache-dir -r requirements.txt

EXPOSE 5500

WORKDIR /app
