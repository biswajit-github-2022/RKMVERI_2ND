sudo chmod -R 777 partitionar
export CLASSPATH="$HADOOP_HOME/share/hadoop/mapreduce/hadoop-mapreduce-client-core-3.2.2.jar:$HADOOP_HOME/share/hadoop/mapreduce/hadoop-mapreduce-client-common-3.2.2.jar:$HADOOP_HOME/share/hadoop/common/hadoop-common-3.2.2.jar:/home/hduser_/programs/MapReduceTutorial/SalesCountry/*:$HADOOP_HOME/lib/*"
javac -d . *.java
jar cfm partitioner.jar Manifest.txt partitionerexample/*.class
$HADOOP_HOME/bin/hdfs dfs -copyFromLocal input.txt /
$HADOOP_HOME/bin/hadoop jar partitioner.jar /input.txt /partitionar_output
$HADOOP_HOME/bin/hdfs dfs -cat /partitionar_output/part-r-00000
