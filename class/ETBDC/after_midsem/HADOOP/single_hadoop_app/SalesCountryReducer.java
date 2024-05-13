package SalesCountry;

import java.io.IOException;
import java.util.Iterator;

import org.apache.hadoop.io.IntWritable;
import org.apache.hadoop.io.Text;
import org.apache.hadoop.mapred.*;

public class SalesCountryReducer extends MapReduceBase implements Reducer<Text, IntWritable, Text, IntWritable> {
    public void reduce(Text key, Iterator<IntWritable> values, OutputCollector<Text, IntWritable> output, Reporter reporter) throws IOException {
        int count = 0;

        // Iterate through the values and count the occurrences
        while (values.hasNext()) {
            count++;
            values.next(); // Move to the next value
        }

        // Emit department and its count
        output.collect(key, new IntWritable(count));
    }
}

