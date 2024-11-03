FROM python:3.9-slim

# Set working directory
WORKDIR /app

# Install necessary packages
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copy the service code
COPY . .

# Run the service
CMD ["python", "app.py"]