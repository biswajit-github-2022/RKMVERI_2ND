import sys
 
from pyspark import SparkContext, SparkConf
 
if __name__ == "__main__":
 
  # create Spark context with Spark configuration
  conf = SparkConf().setAppName("Read Text to RDD - Python")
  sc = SparkContext(conf=conf)
 
  # read input text file to RDD
  lines = sc.textFile("data/rdd/input/sample.txt")
 
  # map lines to n_words
  n_words = lines.map(lambda line : len(line.split()))
 
  # collect the RDD to a list
  llist = n_words.collect()
 
  # print the list
  for line in llist:
    print line
