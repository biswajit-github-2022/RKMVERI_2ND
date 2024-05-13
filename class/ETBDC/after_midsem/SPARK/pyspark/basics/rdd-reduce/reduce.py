import sys
 
from pyspark import SparkContext, SparkConf
 
if __name__ == "__main__":
 
  # create Spark context with Spark configuration
  conf = SparkConf().setAppName("Read Text to RDD - Python")
  sc = SparkContext(conf=conf)
 
  # read input text file to RDD
  numbers = sc.parallelize([1,7,8,9,5,77,48])
 
  # aggregate RDD elements using addition function
  sum = numbers.reduce(lambda a,b:a+b)
 
  print("sum is : " + str(sum))
