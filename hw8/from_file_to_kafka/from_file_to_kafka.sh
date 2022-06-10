docker build -f ./Dockerfile.from_file_to_kafka . -t kafka_write:1.0
docker run --network kafka-network --rm kafka_write:1.0