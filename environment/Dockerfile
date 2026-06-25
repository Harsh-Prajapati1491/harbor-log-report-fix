FROM python:3.11-slim-bookworm@sha256:1a84f509b552e18fa4fc790327f9999336bc17676e1a49f7e8a9cf2976b97ec7

RUN pip install --no-cache-dir \
    pytest==8.4.1 \
    pytest-json-ctrf==0.3.5

WORKDIR /app

COPY access.log /app/access.log
