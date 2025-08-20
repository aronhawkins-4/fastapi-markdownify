# Use official Python image as base
FROM python:3.11-slim

# Copy requirements if present, else skip
COPY requirements.txt .
RUN echo "Installing dependencies..."
RUN pip install --upgrade pip
# Install dependencies if requirements.txt exists
RUN pip install --no-cache-dir -r requirements.txt;

# Copy all project files
COPY . .

# Default command (update as needed)
CMD ["python", "main.py"]