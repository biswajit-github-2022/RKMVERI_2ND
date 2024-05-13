sudo chmod -R 777 topN
export CLASSPATH="$HADOOP_HOME/share/hadoop/mapreduce/hadoop-mapreduce-client-core-3.2.2.jar:$HADOOP_HOME/share/hadoop/mapreduce/hadoop-mapreduce-client-common-3.2.2.jar:$HADOOP_HOME/share/hadoop/common/hadoop-common-3.2.2.jar:/home/hduser_/programs/MapReduceTutorial/SalesCountry/*:$HADOOP_HOME/share/hadoop/hdfs/lib/commons-cli-1.2.jar:$HADOOP_HOME/share/hadoop/common/lib/commons-cli-1.2.jar:$HADOOP_HOME/lib/*"
javac -d . *.java
jar cfm topN.jar Manifest.txt *.class
$HADOOP_HOME/bin/hdfs dfs -copyFromLocal input.txt /
$HADOOP_HOME/bin/hadoop jar topN.jar /input.txt /topN_output
$HADOOP_HOME/bin/hdfs dfs -copyToLocal /topN_output ./

