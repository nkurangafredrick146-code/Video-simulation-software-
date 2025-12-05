FROM python:3.12-slim

WORKDIR /app
COPY . .

# Install dependencies
RUN pip install --upgrade pip && \
    pip install -r requirements.txt

# Default command
CMD ["python", "app.py"]