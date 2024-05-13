export CLASSPATH="$HADOOP_HOME/share/hadoop/mapreduce/hadoop-mapreduce-client-core-3.2.2.jar:$HADOOP_HOME/share/hadoop/mapreduce/hadoop-mapreduce-client-common-3.2.2.jar:$HADOOP_HOME/share/hadoop/common/hadoop-common-3.2.2.jar:$HADOOP_HOME/lib/*"
javac -d . *.java
jar cfm Product.jar Manifest.txt *.class
$HADOOP_HOME/bin/hdfs dfs -copyFromLocal *.txt /
$HADOOP_HOME/bin/hadoop jar Product.jar /name.txt /rec.txt /mapreduce_output
$HADOOP_HOME/bin/hdfs dfs -copyToLocal /mapreduce_output_sales ./
