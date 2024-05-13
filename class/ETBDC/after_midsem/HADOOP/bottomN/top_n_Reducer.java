import java.io.IOException; 
import org.apache.hadoop.io.LongWritable; 
import org.apache.hadoop.io.Text; 
import org.apache.hadoop.mapreduce.Reducer; 
import org.apache.hadoop.conf.Configuration; 
  
public class top_n_Reducer extends Reducer<LongWritable, 
                            Text, LongWritable, Text> { 
  
    static int count; 
  
    @Override
    public void setup(Context context) throws IOException, 
                                     InterruptedException 
    { 
  
        Configuration conf = context.getConfiguration(); 
  
        // we will use the value passed in myValue at runtime 
        String param = conf.get("myValue"); 
  
        // converting the String value to integer 
        count = Integer.parseInt(param); 
    } 
  
    @Override
    public void reduce(LongWritable key, Iterable<Text> values, 
     Context context) throws IOException, InterruptedException 
    { 
  
        long no_of_views =  key.get(); 
        String movie_name = null; 
  
        for (Text val : values) { 
            movie_name = val.toString(); 
        } 
  
        // we just write 10 records as output 
        if (count > 0) 
        { 
            context.write(new LongWritable(no_of_views), 
                                  new Text(movie_name)); 
            count--; 
        } 
    } 
}
