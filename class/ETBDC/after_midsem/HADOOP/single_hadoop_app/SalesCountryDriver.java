package SalesCountry;

import org.apache.hadoop.fs.Path;
import org.apache.hadoop.io.*;
import org.apache.hadoop.mapred.*;

public class SalesCountryDriver {
    public static void main(String[] args) {
        try {
            // Job for processing data with SalesMapper
            JobConf job1 = new JobConf(SalesCountryDriver.class);
            job1.setJobName("Sales Data Processing");
            job1.setOutputKeyClass(Text.class);
            job1.setOutputValueClass(IntWritable.class);
            job1.setMapperClass(SalesCountry.SalesMapper.class);
            job1.setReducerClass(SalesCountry.SalesCountryReducer.class);
            job1.setInputFormat(TextInputFormat.class);
            job1.setOutputFormat(TextOutputFormat.class);
            FileInputFormat.setInputPaths(job1, new Path(args[0]));
            FileOutputFormat.setOutputPath(job1, new Path(args[1] + "/sales"));

            // Job for processing data with AnotherMapper
            JobConf job2 = new JobConf(SalesCountryDriver.class);
            job2.setJobName("Another Data Processing");
            job2.setOutputKeyClass(Text.class);
            job2.setOutputValueClass(IntWritable.class);
            job2.setMapperClass(SalesCountry.AnotherMapper.class);
            job2.setReducerClass(SalesCountry.SalesCountryReducer.class);
            job2.setInputFormat(TextInputFormat.class);
            job2.setOutputFormat(TextOutputFormat.class);
            FileInputFormat.setInputPaths(job2, new Path(args[0]));
            FileOutputFormat.setOutputPath(job2, new Path(args[1] + "/another"));

            // Run both jobs
            JobClient.runJob(job1);
            JobClient.runJob(job2);
        } catch (Exception e) {
            e.printStackTrace();
        }
    }
}

