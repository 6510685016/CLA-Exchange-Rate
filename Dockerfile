FROM python:3.11-slim

WORKDIR /cli_app

COPY . .

RUN pip install --no-cache-dir -r requirements.txt
RUN pip install -e .

RUN cli-exc help