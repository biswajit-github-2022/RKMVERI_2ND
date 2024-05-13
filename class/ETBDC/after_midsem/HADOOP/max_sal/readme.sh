export CLASSPATH="$HADOOP_HOME/share/hadoop/mapreduce/hadoop-mapreduce-client-core-3.2.2.jar:$HADOOP_HOME/share/hadoop/mapreduce/hadoop-mapreduce-client-common-3.2.2.jar:$HADOOP_HOME/share/hadoop/common/hadoop-common-3.2.2.jar:/home/hduser_/programs/employee/*:$HADOOP_HOME/lib/*:/home/hduser_/hadoop/share/hadoop/common/lib/commons-cli-1.2.jar"
javac -d . MaxSalaryMapper.java MaxSalaryReducer.java MaxSalaryDriver.java
jar cfm employee.jar Manifest.txt *.class
$HADOOP_HOME/bin/hdfs dfs -copyFromLocal employee.txt /
$HADOOP_HOME/bin/hadoop jar employee.jar /employee.txt /max_output
$HADOOP_HOME/bin/hdfs dfs -copyToLocal /max_output ./

