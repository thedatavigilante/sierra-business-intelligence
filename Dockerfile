# business-intelligence — Containerized Data Science Portfolio
FROM python:3.10-slim

WORKDIR /app

# Install system deps for data science
RUN apt-get update && apt-get install -y \
    gcc \
    g++ \
    libgomp1 \
    curl \
    && rm -rf /var/lib/apt/lists/*

# Copy and install Python deps
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copy project
COPY . .

# Expose all dashboard ports
EXPOSE 8521
EXPOSE 8522
EXPOSE 8523

# Default: show available dashboards
CMD ["python", "-c", "\nprint('  streamlit run netflix -> http://localhost:8521')\nprint('  streamlit run amazon -> http://localhost:8522')\nprint('  streamlit run google-trends -> http://localhost:8523')\n"]
