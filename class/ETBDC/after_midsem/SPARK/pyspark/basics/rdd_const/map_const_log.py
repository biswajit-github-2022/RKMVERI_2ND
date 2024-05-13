import sys, math
 
from pyspark import SparkContext, SparkConf
 
if __name__ == "__main__":
 
  # create Spark context with Spark configuration
  conf = SparkConf().setAppName("Map Numbers to their Log Values - Python")
  sc = SparkContext(conf=conf)
 
  # read input text file to RDD
  numbers = sc.parallelize([14,21,88,99,455])
 
  # map lines to n_words
  log_values = numbers.map(lambda n : math.log10(n))
 
  # collect the RDD to a list
  llist = log_values.collect()
 
  # print the list
  for line in llist:
    print (line)
