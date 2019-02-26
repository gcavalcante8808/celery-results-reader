FROM python:3.6-slim
WORKDIR /usr/src
COPY requirements.txt .
RUN apt-get update && \
    apt-get install --no-install-recommends -y libev-dev libc-dev gcc && \
    rm -rf /var/lib/aopt/lists/* && \
    apt-get clean
RUN pip install -r requirements.txt
COPY src .
CMD ["python3","wsgi_bjoern.py"]
USER nobody
