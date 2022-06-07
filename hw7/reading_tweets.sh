docker build -f Dockerfile.read . -t kafka_read:1.0
docker run --network kafka-network -v /home/valeriia/big_data_course/big_data_/big_data_course/hw7:/hw7 --rm kafka_read:1.0