mvn clean install -Dhttps.protocols=TLSv1.2

hadoop fs -mkdir /dcache
hadoop fs -mkdir /dcache/input
hadoop fs -copyFromLocal input/lyrics.txt /dcache/input/
hadoop fs -copyFromLocal input/stopWords.txt /dcache/input/
hadoop jar target/dcache.jar /dcache/input/lyrics.txt /dcache/output
