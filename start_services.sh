#!/bin/bash

# Start the Flask API server in the background
python api_server.py &

# Start the Streamlit app
streamlit run app.py
