from pyspark.sql import SparkSession 

# Initialize Spark session
spark = SparkSession.builder.appName("RealDataWordCount").getOrCreate()

# Load real dataset from HDFS
data = spark.read.text("hdfs:///user/bda/Beauty_and_Personal_Care.jsonl")
print("Real Data Loaded Successfully!")

# Perform word count
words = data.rdd.flatMap(lambda line: line.value.split())

# Filter words to exclude metadata keys and unwanted characters
filtered_words = words.filter(lambda word: not word.startswith(("'", '"', '{', '[')) and word.isalpha() and "'" not in word)
word_counts = filtered_words.map(lambda word: (word.lower(), 1)).reduceByKey(lambda a, b: a + b)
sorted_word_counts = word_counts.sortBy(lambda x: x[1], ascending=False)

# Save results to HDFS
sorted_word_counts.saveAsTextFile("hdfs:///user/bda/output_real_spark3")
print("Word Count Completed on Real Data and Results Saved!")
