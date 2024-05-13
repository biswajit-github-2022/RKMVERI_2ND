import org.apache.hadoop.conf.Configuration;
import org.apache.hadoop.conf.Configured;
import org.apache.hadoop.fs.Path;
import org.apache.hadoop.io.LongWritable;
import org.apache.hadoop.io.Text;
import org.apache.hadoop.mapreduce.Job;
import org.apache.hadoop.mapreduce.lib.input.MultipleInputs;
import org.apache.hadoop.mapreduce.lib.input.TextInputFormat;
import org.apache.hadoop.mapreduce.lib.output.FileOutputFormat;
import org.apache.hadoop.util.Tool;
import org.apache.hadoop.util.ToolRunner;
public class MultipleInputDriver extends Configured implements Tool
{
@Override
public int run(String[] args) throws Exception
{
int status = -1;
Configuration configuration = getConf();
//Setting the Separator for parsing TAB separated input file 1 for MultipleInputMapper1
configuration.set("Separator.File1", "\t");
//Setting the separator for parsing ";" separated input file 2 for MultipleInputMapper2
configuration.set("Separator.File2", ";");
//Setting the separator for Reducer for saving the file into TAB separated output file.
configuration.set("Separator.Common", "\t");
Job job = new Job(configuration, "Multiple Input Example");
//TAB separated input File 1
MultipleInputs.addInputPath(job,new Path(args[0]), TextInputFormat.class, MultipleInputMapper1.class);
//";" separated input file 2
MultipleInputs.addInputPath(job, new Path(args[1]), TextInputFormat.class, MultipleInputMapper2.class);
job.setJarByClass(MultipleInputDriver.class);
job.setReducerClass(MultipleInputReducer.class);
job.setMapOutputKeyClass(LongWritable.class);
job.setMapOutputValueClass(Text.class);
job.setOutputKeyClass(LongWritable.class);
job.setOutputValueClass(Text.class);
FileOutputFormat.setOutputPath(job, new Path(args[2]));
job.waitForCompletion(true);
status = job.isSuccessful()? 0:-1;
return status;
}
public static void main(String [] args)
{
int result;
try{
result= ToolRunner.run(new Configuration(), new MultipleInputDriver(), args);
if(0 == result)
{
System.out.println("Job completed Successfully...");
}
else
{
System.out.println("Job Failed...");
}
}
catch(Exception exception)
{
exception.printStackTrace();
}
}
}
