from pyspark.sql import SparkSession
import time


spark = SparkSession.builder \
    .appName("MyJob") \
    .master("spark://spark-master:7077") \
    .config("spark.executor.cores", "2") \
    .config("spark.cores.max", "4") \
    .config("spark.executor.memory", "2g") \
    .getOrCreate()
# Simulate a long-running job


time.sleep(5000)
spark.stop()