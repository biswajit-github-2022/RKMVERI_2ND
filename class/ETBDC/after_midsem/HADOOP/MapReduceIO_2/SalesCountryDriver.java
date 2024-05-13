package SalesCountry;

import org.apache.hadoop.fs.Path;
import org.apache.hadoop.io.*;
//import org.apache.hadoop.mapred.*;
import org.apache.hadoop.mapreduce.*;
import org.apache.hadoop.mapreduce.lib.input.*;
import org.apache.hadoop.mapreduce.lib.output.*;
import org.apache.hadoop.conf.*;
import org.apache.hadoop.util.*;

import java.lang.reflect.*;

public class SalesCountryDriver extends Configured implements Tool {

      	public void reflectMe(Class c)
      	{
         	try {
            		//Class c = Class.forName(args[0]);
            		Method m[] = c.getDeclaredMethods();
            		for (int i = 0; i < m.length; i++)
            			System.out.println(m[i].toString());
         		}
         	catch (Throwable e) {
            		System.err.println(e);
         	}
      	}
      	public void reflectMe(String arg)
      	{
            		System.out.println("From String called");
         	try {
            		Class c = Class.forName(arg);
            		Method m[] = c.getDeclaredMethods();
            		System.out.println("From String");
            		for (int i = 0; i < m.length; i++)
            			System.out.println(m[i].toString());
         		}
         	catch (Throwable e) {
            		System.err.println(e);
         	}
      	}
    	public static void main(String[] args) throws Exception {
	    	int res = ToolRunner.run(new Configuration(), new SalesCountryDriver(), args);
	    	System.exit(0);
	}

    	@Override
    	public int run(String[] args) throws Exception
    	{
	    	Thread.dumpStack();
    		Configuration conf = getConf();
        	Job job = Job.getInstance(conf, "SalesCalc");
		job.setJarByClass(getClass());

    		job.setMapperClass(SalesCountry.SalesMapper.class);
    		job.setReducerClass(SalesCountry.SalesCountryReducer.class);
    		job.setOutputKeyClass(Text.class);
    		job.setMapOutputKeyClass(LongWritable.class);
    		job.setMapOutputValueClass(Text.class);
    		job.setOutputValueClass(Text.class);
      		//job.setInputFormatClass(TextInputFormat.class);
		job.setInputFormatClass(CustomInputFormat.class);
		job.setOutputFormatClass(File_OutputFormat.class);

		//job.setNumReduceTasks(4);

      		//job.setOutputFormatClass(TextOutputFormat.class);
		//job.setPartitionerClass(SalesPartitioner.class);

        	FileInputFormat.setInputPaths(job, new Path(args[0]));
        	FileOutputFormat.setOutputPath(job, new Path(args[1]));

		this.reflectMe(getClass());
		this.reflectMe("SalesCountry.SalesCountryDriver");
		return job.waitForCompletion(true) ? 0 : 1;
    }
}
