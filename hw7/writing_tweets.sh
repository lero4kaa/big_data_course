docker build -f ./Dockerfile.write . -t kafka_write:1.0
docker run --network kafka-network --rm kafka_write:1.0