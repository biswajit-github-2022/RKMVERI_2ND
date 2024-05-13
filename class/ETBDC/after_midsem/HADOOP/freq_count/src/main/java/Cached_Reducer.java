package word_count_DC;

import java.io.*;
import org.apache.hadoop.io.Text;
import org.apache.hadoop.io.LongWritable;
import org.apache.hadoop.mapreduce.Reducer;


public class Cached_Reducer extends Reducer<Text,LongWritable,Text,LongWritable> {

	public void reduce(Text key, Iterable<LongWritable> values ,Context context)throws IOException,InterruptedException
	{
		long sum=0;
		
		for(LongWritable val:values)
		{
			sum+= val.get();
		}
		
		context.write(key,new LongWritable(sum));
		
		
		
	}
	
	
	
}