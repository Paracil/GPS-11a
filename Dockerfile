#Base image for the python application
FROM python:3.11-slim

WORKDIR /app

# Install dependencies
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY . .

# Default command for running tests
CMD ["python", "-m", "unittest", "discover", "-s", ".", "-p", "test*.py"]