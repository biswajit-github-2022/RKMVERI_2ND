sudo chmod -R 777 MapReduceIO_2
export CLASSPATH="$HADOOP_HOME/share/hadoop/mapreduce/hadoop-mapreduce-client-core-3.2.2.jar:$HADOOP_HOME/share/hadoop/mapreduce/hadoop-mapreduce-client-common-3.2.2.jar:$HADOOP_HOME/share/hadoop/common/hadoop-common-3.2.2.jar:$HADOOP_HOME/lib/*"
javac -d . *.java
jar cfm ProductSalePerCountry.jar Manifest.txt SalesCountry/*.class
$HADOOP_HOME/bin/hdfs dfs -copyFromLocal input/input_reader.txt /
$HADOOP_HOME/bin/hadoop jar ProductSalePerCountry.jar /input_reader.txt /mapreduce_output_sales
$HADOOP_HOME/bin/hdfs dfs -cat /other.log
$HADOOP_HOME/bin/hdfs dfs -cat /xyz.log

$HADOOP_HOME/bin/hdfs dfs -copyToLocal /topN_output ./
