Place twcs.csv file in hw7 folder.  

Create containers:

```
docker-compose up -d
```

In one terminal window start container for consumer:
```
sh reading_tweets.sh 
```

In another terminal window start container with producer:
```
sh writing_tweets.sh 
```

Check all containers with docker ps:
```
docker ps
```
![alt text](https://github.com/lero4kaa/big_data_course/blob/master/hw7/screenshots/containers.jpg?raw=true)

All csv files are saved in tweets_files folder. Check them:

```
ls tweets_files/
```
![alt text](https://github.com/lero4kaa/big_data_course/blob/master/hw7/screenshots/list_of_created_files.jpg?raw=true)

Examples of files:
![alt text](https://github.com/lero4kaa/big_data_course/blob/master/hw7/screenshots/csv1.jpg?raw=true)
![alt text](https://github.com/lero4kaa/big_data_course/blob/master/hw7/screenshots/csv2.jpg?raw=true)

