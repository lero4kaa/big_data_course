docker build -f ./Dockerfile.from_kafka_to_cassandra . -t cassandra_write:1.0
docker run --network kafka-network --rm cassandra_write:1.0