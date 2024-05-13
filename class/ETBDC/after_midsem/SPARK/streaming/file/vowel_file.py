from pyspark.sql import SparkSession
from pyspark.sql.functions import split, explode, window, current_timestamp, udf
from pyspark.sql.types import IntegerType

# Create SparkSession
spark = SparkSession.builder \
    .appName("MovingAverageStreamingFromFile") \
    .getOrCreate()

# Define a custom function to count vowels in a word
def count_vowels(word):
    vowels = "aeiouAEIOU"
    return sum(1 for letter in word if letter in vowels)

# Register the custom function as a UDF
count_vowels_udf = udf(count_vowels, IntegerType())

# Read streaming data from a file (initial path)
#initial_path = "file:///path/to/initial/file"
initial_path = "file:////home/champak/sw/Distributed/spark/stream/file/test_file.txt"
lines = spark.readStream \
    .format("text") \
    .load(initial_path)

# Split the lines into words and add a timestamp
words = lines.select(explode(split(lines.value, " ")).alias("word"), current_timestamp().alias("timestamp"))

# Apply the custom function to count vowels in each word
words_with_vowel_count = words.withColumn("vowel_count", count_vowels_udf(words.word))

# Define a sliding window of 10 seconds with a slide duration of 5 seconds
windowedAvgVowelCount = words_with_vowel_count \
    .groupBy(window(words_with_vowel_count.timestamp, "10 seconds", "5 seconds")) \
    .agg({"vowel_count": "avg"})

# Output the moving average of vowel counts to the console
query = windowedAvgVowelCount \
    .writeStream \
    .outputMode("complete") \
    .format("console") \
    .start()

# Wait for the streaming to finish
query.awaitTermination()

# Stop the SparkSession
spark.stop()

