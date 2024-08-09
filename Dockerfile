FROM python:3.9.6-slim

RUN apt-get update && \
    apt-get upgrade -y && \
    apt-get install -y git && \
    apt-get install -y build-essential

RUN mkdir -p /usr/src/app
WORKDIR /usr/src/app

ARG XRPL_FAUCET_URL
ENV XRPL_FAUCET_URL $XRPL_FAUCET_URL
ARG XRPL_NETWORK_ID
ENV XRPL_NETWORK_ID $XRPL_NETWORK_ID

COPY requirements.txt /usr/src/app/

RUN pip3 install --no-cache-dir -r requirements.txt

COPY . /usr/src/app

EXPOSE 8080

CMD exec gunicorn --bind :8080 --workers 1 swagger_server:app --timeout 3600