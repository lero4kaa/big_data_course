docker build -f ./Dockerfile.app . -t cassandra_write:1.0
docker run --network kafka-network --rm cassandra_write:1.0