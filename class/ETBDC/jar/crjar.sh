javac Class1.java
javac Class2.java
javac Class3.java
javac MainClass.java
jar cfm MyProgram.jar manifest.txt *.class
javac -cp .:MyProgram.jar UserClass.java
java -cp .:MyProgram.jar UserClass
