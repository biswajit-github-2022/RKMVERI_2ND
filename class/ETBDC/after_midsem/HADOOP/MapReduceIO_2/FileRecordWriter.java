
package SalesCountry;


import org.apache.hadoop.fs.FSDataOutputStream;
import org.apache.hadoop.fs.FileSystem;
import org.apache.hadoop.fs.Path;
import org.apache.hadoop.io.IOUtils;
import org.apache.hadoop.io.LongWritable;
import org.apache.hadoop.io.Text;
import org.apache.hadoop.mapreduce.RecordWriter;
import org.apache.hadoop.mapreduce.TaskAttemptContext;
import java.nio.charset.StandardCharsets;

import java.io.IOException;

public class FileRecordWriter extends RecordWriter<LongWritable, Text> {
    FSDataOutputStream atguiguOut = null;
    FSDataOutputStream otherOut = null;
    private Text fieldSeparator;
    private Text recSeparator;
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
	this.recSeparator = new Text("\n");
	this.fieldSeparator = new Text("\t\t");
	System.out.println("WRITER CALLED");
    }
    @Override
    public void write(LongWritable key, Text value) throws IOException, InterruptedException {

        //  Determine whether to include "atguigu" and output to different files
	System.out.println("write CALLED");
	LongWritable div = new LongWritable(1205);
	if (key.compareTo(div) > 0) {
            atguiguOut.write(key.toString().getBytes());
            atguiguOut.write(this.fieldSeparator.toString().getBytes());
            atguiguOut.write(value.toString().getBytes());
            atguiguOut.write(this.recSeparator.toString().getBytes());
        } else {
            otherOut.write(key.toString().getBytes());
            otherOut.write(this.fieldSeparator.toString().getBytes());
            otherOut.write(value.toString().getBytes());
            otherOut.write(this.recSeparator.toString().getBytes());
        }
    }
    @Override
    public void close(TaskAttemptContext context) throws IOException, InterruptedException {
        //  Close resource
        IOUtils.closeStream(atguiguOut);
        IOUtils.closeStream(otherOut);
    }
}

