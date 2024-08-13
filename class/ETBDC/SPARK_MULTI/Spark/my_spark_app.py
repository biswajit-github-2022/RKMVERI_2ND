# Import necessary modules
from pyspark.sql import SparkSession, Row
from pyspark.sql.functions import udf
from pyspark.sql.types import StructType, StructField, StringType, LongType
from transformers import AutoTokenizer, AutoModelForSeq2SeqLM
import pandas as pd

# Create a Spark session
spark = SparkSession.builder \
    .appName("FlanT5Seq2SeqExample") \
    .master("spark://172.20.251.77:7077") \
    .getOrCreate()

# Define schema for the DataFrame
schema = StructType([
    StructField("id", LongType(), nullable=False),
    StructField("sentence", StringType(), nullable=False)
])

"""
# Sample data for the DataFrame
data = [
  Row(1, "It is a good test for Spark."),
  Row(2, "Spark DataFrames are powerful."),
  Row(3, "LLMs could be very slow."),
  Row(4, "It is a naive statement."),
  Row(5, "LLMs can be misleading sometimes."),
  Row(6, "Football is the best sport"),
  Row(7, "Computer lab is not up to date"),
  Row(8, "Exams are very nearby"),
  Row(9, "AI is a book to mankind"),
  Row(10, "A pen is mightier than a sword"),
  Row(11, "Twinkle Twinkle Little Starr"),
  Row(12, "The Atom bomb was the endpoint of the World War 2 which saved many American Lives"),
  Row(13, "Night is a very scary time to walk around alone"),
  Row(14, "RGB mouse and keyboards look better than normal devices"),
  Row(15, "Out of 30 computers in the Lab, only 10 work properly"),
  Row(16, "10 computers out of 30 in the Lab works very good"),
  Row(17, "My name is Khan")
]
"""
csv_path = "/home/hduser_/Desktop/tweetsBJP.csv"

# Create a Spark DataFrame
#input_df = spark.createDataFrame(data,schema=schema)
input_df = spark.read.csv(csv_path, header=False, inferSchema=True)
input_df = input_df.withColumnRenamed("_c0", "sentence")  # Assuming only one column in CSV containing text

# Loading Flan T5 Model and Tokenizer
model = AutoModelForSeq2SeqLM.from_pretrained("google/flan-t5-small")
tokenizer = AutoTokenizer.from_pretrained("google/flan-t5-small")

# Defining the Spark UDF
def t5_seq2seq_udf(input_text):
    prompt = f"sentiment of the text: {input_text}"
    input = tokenizer(prompt, return_tensors="pt")
    output = model.generate(**input)
    output_text = tokenizer.decode(output[0], skip_special_tokens=True)
    return output_text

# Register the Spark UDF
t5_udf = udf(t5_seq2seq_udf, returnType=StringType())

# Apply the UDF to the DataFrame
results_df = input_df.withColumn('output_column', t5_udf(input_df['sentence']))

# Show the results
results_df.show(truncate=False)

# Stop the Spark session
spark.stop()
