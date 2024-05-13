
package SalesCountry;

import java.io.IOException;
import org.apache.hadoop.io.*;
import org.apache.hadoop.mapred.*;

public class AnotherMapper extends MapReduceBase implements Mapper<LongWritable, Text, Text, IntWritable> {
    private final static IntWritable one = new IntWritable(1);

    public void map(LongWritable key, Text value, OutputCollector<Text, IntWritable> output, Reporter reporter) throws IOException {
        String valueString = value.toString();
        String[] data = valueString.split(",");

        // Assuming the department information is stored in a specific column (e.g., the 8th column)
        String department = data[7].trim(); // Extracting department from 8th column

        // Emit key-value pair where key is the department and value is one
        output.collect(new Text(department), one);
    }
}

