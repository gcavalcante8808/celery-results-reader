FROM python:3.6-slim
WORKDIR /usr/src
COPY requirements.txt .
RUN pip install -r requirements.txt