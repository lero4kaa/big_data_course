File PS_20174392719_1491204439457_log.csv should be in this folder (hw9).

Start containers with docker-compose:
````
docker-compose up -d
````
Result:
```
docker ps
```
![alt text](https://github.com/lero4kaa/big_data_course/blob/master/hw9/screenshots/containers.jpg?raw=true)

Run spark program with:
```
sh process_data.sh
```
Result:
![alt text](https://github.com/lero4kaa/big_data_course/blob/master/hw9/screenshots/result.jpg?raw=true)

Shutdown containers with docker-compose:
```
docker-compose down
```