from pyspark.sql import SparkSession

spark = SparkSession.builder.appName("PythonWordCount").getOrCreate()

text = "AM I A JOKE TO YOU"

words = spark.sparkContext.parallelize(text.split(" "))

wordCounts = words.map(lambda word: (word, 1)).reduceByKey(lambda a, b: a + b)

for wc in wordCounts.collect():
    print(wc[0], wc[1])

spark.stop() 