sudo chmod -R 777 bottomN
export CLASSPATH="$HADOOP_HOME/share/hadoop/mapreduce/hadoop-mapreduce-client-core-3.2.2.jar:$HADOOP_HOME/share/hadoop/mapreduce/hadoop-mapreduce-client-common-3.2.2.jar:$HADOOP_HOME/share/hadoop/common/hadoop-common-3.2.2.jar:/home/hduser_/programs/MapReduceTutorial/SalesCountry/*:$HADOOP_HOME/share/hadoop/hdfs/lib/commons-cli-1.2.jar:$HADOOP_HOME/share/hadoop/common/lib/commons-cli-1.2.jar:$HADOOP_HOME/lib/*"
javac -d . *.java
jar cfm bottomN.jar Manifest.txt *.class
$HADOOP_HOME/bin/hdfs dfs -copyFromLocal input.txt /
$HADOOP_HOME/bin/hadoop jar bottomN.jar /input.txt /bottomN_output
$HADOOP_HOME/bin/hdfs dfs -copyToLocal /bottomN_output ./
