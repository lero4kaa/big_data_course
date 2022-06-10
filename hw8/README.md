File PS_20174392719_1491204439457_log.csv should be placed in the folder hw8/from_file_to_kafka.

## Commands to run ##
Start kafka containers:

```
sh kafka/run-kafka-cluster.sh 
```

Start cassandra container:
```
sh cassandra/run-cassandra-cluster.sh
```

Check containers:

```
docker ps
```

![alt text](https://github.com/lero4kaa/big_data_course/blob/master/hw8/screenshots/containers_run.jpg?raw=true)

Create topic in kafka:
```
sh kafka/topic-creation.sh 
```

Change folder to cassandra/ and run script to create tables in cassandra (it might take some time to connect):
```
cd cassandra/
sh ddl.sh
``` 

![alt text](https://github.com/lero4kaa/big_data_course/blob/master/hw8/screenshots/ddl.jpg?raw=true)

In new terminal window change folder to from_kafka_to_cassandra and start script that receives messages from kafka and insert them to cassandra tables:

```
cd from_kafka_to_cassandra/
sh from_kafka_to_cassandra.sh 
```

![alt text](https://github.com/lero4kaa/big_data_course/blob/master/hw8/screenshots/start_consumer.jpg?raw=true)

In another terminal window change folder to from_file_to_kafka/ and start script that reads data from file and sends it to kafka:

```
cd from_file_to_kafka/
sh from_file_to_kafka.sh 
```
![alt text](https://github.com/lero4kaa/big_data_course/blob/master/hw8/screenshots/start_producer.jpg?raw=true)

In new terminal window change folder to app_api/ and start script that runs api:
```
cd app_api/
sh app_api.sh
```
![alt text](https://github.com/lero4kaa/big_data_course/blob/master/hw8/screenshots/start_app.jpg?raw=true)

Stop all processes and then shutdown containers:
```
sh cassandra/shutdown-cassandra-cluster.sh
sh kafka/shutdown-kafka-cluster.sh 
```
![alt text](https://github.com/lero4kaa/big_data_course/blob/master/hw8/screenshots/containers_shutdown.jpg?raw=true)

## Examples of API requests ##

1. All transactions of the user that were marked as fraud:

![alt text](https://github.com/lero4kaa/big_data_course/blob/master/hw8/screenshots/request1.jpg?raw=true)

2. 3 largest transactions of the user:

![alt text](https://github.com/lero4kaa/big_data_course/blob/master/hw8/screenshots/request2.jpg?raw=true)

3. The sum of all transactions received by the user:

![alt text](https://github.com/lero4kaa/big_data_course/blob/master/hw8/screenshots/request3.jpg?raw=true)

## Connection generator - Kafka - user ##

Data is read from the file and sent to Kafka-consumer:

![alt text](https://github.com/lero4kaa/big_data_course/blob/master/hw8/screenshots/generator.jpg?raw=true)

Data is received by Kafka-consumer and is inserted to Cassandra:

![alt text](https://github.com/lero4kaa/big_data_course/blob/master/hw8/screenshots/kafka_consumer.jpg?raw=true)

Data can be received by API request:

![alt text](https://github.com/lero4kaa/big_data_course/blob/master/hw8/screenshots/user.jpg?raw=true)
