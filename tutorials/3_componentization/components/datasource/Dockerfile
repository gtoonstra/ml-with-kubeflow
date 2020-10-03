FROM python:3.7.9
RUN pip install --upgrade pip setuptools wheel
COPY extract_data.py /component/extract_data.py
COPY simulated_data.csv /simulated_data.csv

# Notice that this container does not have an entrypoint...
# Entrypoints are for running containers that run services.
