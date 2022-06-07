from datetime import datetime
import csv
from kafka import KafkaConsumer
from json import loads


consumer = KafkaConsumer('tweets', bootstrap_servers= 'kafka-server:9092', 
                         value_deserializer=lambda x: loads(x.decode('utf-8')))

curr_date = ''
message_for_cur_date = []

for message in consumer:
    message_date_str = datetime.strftime(datetime.strptime(message.value['created_at'], '%a %b %d %H:%M:%S %Y'), '%a %b %d %H:%M %Y')
    message_lst = [message.value['author_id'], message.value['created_at'], message.value['text']]
    
    if not curr_date:
        curr_date = message_date_str

    if message_date_str != curr_date:
        curr_date = datetime.strptime(curr_date, '%a %b %d %H:%M %Y')
        with open(f'tweets_files/tweets_{curr_date.day}_{curr_date.month}_{curr_date.year}_{curr_date.hour}_{curr_date.minute}.csv', 'w') as f:
            write = csv.writer(f, delimiter=',')
            write.writerows(message_for_cur_date)
        message_for_cur_date = [message_lst]
        curr_date = message_date_str

    else:
        message_for_cur_date.append(message_lst)
