# Base image
FROM python:3.11-slim

# Set the working directory
WORKDIR /app

# Copy requirements.txt
COPY requirements.txt .

# Install dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Copy the rest of the app files
COPY . .

# Expose the ports that Streamlit and Flask use
EXPOSE 8501
EXPOSE 5000


ENV STREAMLIT_SERVER_HEADLESS=true
ENV STREAMLIT_SERVER_ENABLE_CORS=false
ENV STREAMLIT_SERVER_ENABLE_XSRF_PROTECTION=false
ENV STREAMLIT_SERVER_PORT=8501
ENV STREAMLIT_SERVER_ADDRESS=0.0.0.0

# Make the start script executable
RUN chmod +x start_services.sh

# Run both the Flask API server and the Streamlit app
CMD ["./start_services.sh"]
