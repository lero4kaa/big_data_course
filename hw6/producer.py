from kafka import KafkaProducer
from json import dumps
import csv
import datetime

producer = KafkaProducer(bootstrap_servers='kafka-server:9092', 
                        api_version=(2,0,2),
                         value_serializer=lambda x:
                         dumps(x).encode('ascii'))

with open('twcs.csv', 'r') as f:
    file = csv.reader(f)
    header = next(file)
    for row in file:
        row[3] = datetime.datetime.now().strftime("%c")
        row = ','.join(row)
        producer.send('tweets', row)
        producer.flush()
