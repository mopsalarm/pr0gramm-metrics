FROM python:3.5-alpine

ENV PYTHONUNBUFFERED 1

COPY requirements.txt /tmp
RUN pip install -r /tmp/requirements.txt

COPY . /app
WORKDIR /app
ENTRYPOINT ["python3", "main.py"]
