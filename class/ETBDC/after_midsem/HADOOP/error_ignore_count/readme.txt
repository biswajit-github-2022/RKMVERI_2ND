sudo chmod -R 777 MapReduceTutorial
export CLASSPATH="$HADOOP_HOME/share/hadoop/mapreduce/hadoop-mapreduce-client-core-3.2.2.jar:$HADOOP_HOME/share/hadoop/mapreduce/hadoop-mapreduce-client-common-3.2.2.jar:$HADOOP_HOME/share/hadoop/common/hadoop-common-3.2.2.jar:/home/hduser_/programs/MapReduceTutorial/SalesCountry/*:$HADOOP_HOME/lib/*"
javac -d . SalesMapper.java SalesCountryReducer.java SalesCountryDriver.java
jar cfm ProductSalePerCountry.jar Manifest.txt SalesCountry/*.class
$HADOOP_HOME/bin/hdfs dfs -copyFromLocal inputMapReduce /

list:
$HADOOP_HOME/bin/hdfs dfs -ls /

removes:
$HADOOP_HOME/bin/hdfs dfs -rm -r /mapreduce_output_sales

$HADOOP_HOME/bin/hadoop jar ProductSalePerCountry.jar /inputMapReduce /mapreduce_output_sales
$HADOOP_HOME/bin/hdfs dfs -copyToLocal /mapreduce_output_sales ./


find /home/hduser_/hadoop -name commons-cli-1.2.jar
