from kafka import KafkaProducer
from json import dumps
import csv
import datetime

producer = KafkaProducer(bootstrap_servers='kafka-server:9092', 
                        api_version=(2,0,2),
                         value_serializer=lambda x:
                         dumps(x).encode('ascii'))

with open('twcs.csv', 'r') as f:
# with open('sample.csv', 'r') as f:
    file = csv.reader(f)
    header = next(file)
    for row in file:
        row[3] = datetime.datetime.now().strftime("%c")
        row = {'author_id': row[1], 'created_at': row[3], 'text': row[4]}
        producer.send('tweets', row)
        producer.flush()
