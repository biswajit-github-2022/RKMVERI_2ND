export CLASSPATH="$HADOOP_HOME/share/hadoop/mapreduce/hadoop-mapreduce-client-core-3.2.2.jar:$HADOOP_HOME/share/hadoop/mapreduce/hadoop-mapreduce-client-common-3.2.2.jar:$HADOOP_HOME/share/hadoop/common/hadoop-common-3.2.2.jar:/home/hduser_/programs/MapReduceTutorial/SalesCountry/*:$HADOOP_HOME/lib/*"


javac -d . *.java
jar cfm Product.jar Manifest.txt com/atguigu/mr/outputformat/*.class
$HADOOP_HOME/bin/hdfs dfs -copyFromLocal input.txt /
hadoop jar Product.jar
$HADOOP_HOME/bin/hdfs dfs -cat /xyz.log
$HADOOP_HOME/bin/hdfs dfs -cat /xyz.log
