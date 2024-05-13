package com.atguigu.mr.outputformat;

import org.apache.hadoop.io.NullWritable;
import org.apache.hadoop.io.Text;
import org.apache.hadoop.mapreduce.Reducer;
import java.io.IOException;

public class FileReducer extends Reducer<Text, NullWritable,Text,NullWritable> {
    Text k = new Text();
    @Override
    protected void reduce(Text key, Iterable<NullWritable> values, Context context)		throws IOException, InterruptedException {
        //  1 Get a row
        String line = key.toString();
        System.out.println(line);
        //  2 splicing
        line = line + "\r\n";
        System.out.println(line);
        //  3 Set the key
        k.set(line);
        //System.out.println(k);
        //  4 output
        context.write(k, NullWritable.get());
    }
}
