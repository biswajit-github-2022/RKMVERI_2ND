package com.atguigu.mr.outputformat;

import org.apache.hadoop.conf.Configuration;
import org.apache.hadoop.fs.Path;
import org.apache.hadoop.io.NullWritable;
import org.apache.hadoop.io.Text;
import org.apache.hadoop.mapreduce.Job;
import org.apache.hadoop.mapreduce.lib.input.FileInputFormat;
import org.apache.hadoop.mapreduce.lib.output.FileOutputFormat;

import java.io.IOException;

public class FileDriver {
    public static void main(String[] args) throws Exception {
        //1 Get the Job object
        Configuration conf = new Configuration();
        Job job = Job.getInstance(conf);

        //2 Set the jar storage location
        job.setJarByClass(FileDriver.class);

        //3 Associate Mapper and Reducer classes
        job.setMapperClass(FileMapper.class);
        job.setReducerClass(FileReducer.class);

        //4 Set the kv type output by the map stage
        job.setMapOutputKeyClass(Text.class);
        job.setMapOutputValueClass(NullWritable.class);

        //5 Set the final output type
        job.setOutputKeyClass(Text.class);
        job.setOutputValueClass(NullWritable.class);

        //6 To set a custom output format component to the job
        job.setOutputFormatClass(File_OutputFormat.class);

        //7 Set input and output path
        FileInputFormat.setInputPaths(job, new Path("/input.txt"));
        //  Although we have customized outputformat, because our outputformat inherits from fileoutputformat
        //  And fileoutputformat wants to output a _SUCCESS file, so here you have to specify an output directory
        FileOutputFormat.setOutputPath(job, new Path("/output777"));

        //8 Submit Job
        boolean result = job.waitForCompletion(true);
        System.exit(result ? 0 : 1);
    }
}
