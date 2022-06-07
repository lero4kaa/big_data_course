First, place twcs.csv file in hw6 folder.

Then create containers with docker-compose and check them with docker ps.
```
docker-compose up -d

docker ps
```

![alt text](https://github.com/lero4kaa/big_data_course/blob/master/hw6/screenshots/containers.jpg?raw=true)

In new terminal start consumer:
```
sh consumer_read.sh
```

In another terminal start app for sending tweets:
```
sh run_app.sh
```
![alt text](https://github.com/lero4kaa/big_data_course/blob/master/hw6/screenshots/app_result.jpg?raw=true)

Then in the terminal with consumer tweets appear:
![alt text](https://github.com/lero4kaa/big_data_course/blob/master/hw6/screenshots/consumer.jpg?raw=true)

Stop and remove containers:
```
docker-compose down
```

![alt text](https://github.com/lero4kaa/big_data_course/blob/master/hw6/screenshots/shut-down.jpg?raw=true)
