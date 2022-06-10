from pyspark.sql import SparkSession
spark = SparkSession.builder.appName('HomeworkProject').getOrCreate()

df = spark.read.csv("PS_20174392719_1491204439457_log.csv")
all_rows = df.count()

print('--------------------------')
print('Number of rows in the file: ', all_rows)
print('--------------------------')