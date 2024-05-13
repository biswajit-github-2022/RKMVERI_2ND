package SalesCountry;

import java.io.IOException;
import java.util.*;

import org.apache.hadoop.io.IntWritable;
import org.apache.hadoop.io.Text;
import org.apache.hadoop.io.LongWritable;
import org.apache.hadoop.mapreduce.*;

public class SalesCountryReducer extends Reducer<LongWritable,Text,LongWritable,Text> {

	static int count = 40;

	@Override
	//public void reduce(Text t_key, Iterator<Text> values, Context context)
	public void reduce(LongWritable key, Iterable<Text> values, Context context)
	        throws IOException, InterruptedException {

		long no_of_views = (-1) * key.get();
        	String movie_name = "";
  
        	for (Text val : values) {
            		movie_name += val.toString();
        	}
  
        	if (count > 0)
        	{
            		context.write(new LongWritable(no_of_views),
                                  new Text(movie_name));
            		count--;
        	}
	}
}
