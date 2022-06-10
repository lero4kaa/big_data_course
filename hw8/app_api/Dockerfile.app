FROM python:3.9-slim

RUN apt-get update

RUN pip install --upgrade pip
RUN pip install kafka-python
RUN pip install flask
RUN pip install cassandra-driver


COPY ./app.py .
COPY ./cassandra_client.py .

CMD [ "python3", "app.py"]