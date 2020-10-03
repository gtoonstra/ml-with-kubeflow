FROM python:3.7.9
RUN pip install --upgrade pip setuptools wheel
RUN python3 -m pip install pandas
COPY preprocess.py /component/preprocess.py

# Notice that this container does not have an entrypoint...
# Entrypoints are for running containers that run services.
