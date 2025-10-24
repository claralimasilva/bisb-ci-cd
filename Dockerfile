FROM python:3.12-slim

WORKDIR /app

# Install dependencies
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copy application
COPY app ./app

# Expose Flask port
EXPOSE 5000

# Run the app
CMD ["python", "-m", "app.main"]