FROM python:3.10.12-slim

WORKDIR /app

RUN pip install flask

COPY server.py /app

CMD ["python", "server.py"]

EXPOSE 5000
