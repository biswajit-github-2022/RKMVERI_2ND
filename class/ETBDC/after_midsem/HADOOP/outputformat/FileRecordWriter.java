package com.atguigu.mr.outputformat;

import org.apache.hadoop.fs.FSDataOutputStream;
import org.apache.hadoop.fs.FileSystem;
import org.apache.hadoop.fs.Path;
import org.apache.hadoop.io.IOUtils;
import org.apache.hadoop.io.NullWritable;
import org.apache.hadoop.io.Text;
import org.apache.hadoop.mapreduce.RecordWriter;
import org.apache.hadoop.mapreduce.TaskAttemptContext;

import java.io.IOException;

public class FileRecordWriter extends RecordWriter<Text, NullWritable> {
    FSDataOutputStream atguiguOut = null;
    FSDataOutputStream otherOut = null;
    public FileRecordWriter(TaskAttemptContext job) {
        //  1 Get the file system
        FileSystem fs;
        try {
            fs = FileSystem.get(job.getConfiguration());
            //  2 Create output file path
            Path atguiguPath = new Path("/xyz.log");
            Path otherPath = new Path("/other.log");
            //  3 Create an output stream
            atguiguOut = fs.create(atguiguPath);
            otherOut = fs.create(otherPath);
        } catch (IOException e) {
            e.printStackTrace();
        }
    }
    @Override
    public void write(Text key, NullWritable value) throws IOException, InterruptedException {

        //  Determine whether to include "atguigu" and output to different files
        if (key.toString().contains("xyz")) {
            atguiguOut.write(key.toString().getBytes());
        } else {
            otherOut.write(key.toString().getBytes());
        }
    }
    @Override
    public void close(TaskAttemptContext context) throws IOException, InterruptedException {
        //  Close resource
        IOUtils.closeStream(atguiguOut);
        IOUtils.closeStream(otherOut);	
    }
}
