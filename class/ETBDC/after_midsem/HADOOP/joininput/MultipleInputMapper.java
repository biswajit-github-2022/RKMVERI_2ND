import java.io.IOException;
import org.apache.hadoop.conf.Configuration;
import org.apache.hadoop.io.LongWritable;
import org.apache.hadoop.io.Text;
import org.apache.hadoop.mapreduce.Mapper;
public class MultipleInputMapper extends Mapper<LongWritable, Text, LongWritable, Text>
{
	private static String separator;
	private static String commonSeparator;
	private String file_tag;

	@Override
	public void map(LongWritable rowKey, Text value,
			Context context) throws IOException, InterruptedException
	{
		String[] values = value.toString().split(separator);
		StringBuilder stringBuilder = new StringBuilder();
		for(int index=1;index<values.length;index++)
		{
			stringBuilder.append(values[index]+commonSeparator);
		}
		if(values[0] != null && !"NULL".equalsIgnoreCase(values[0]))
		{
			context.write(new LongWritable(Long.parseLong(values[0])), new Text(file_tag+commonSeparator+stringBuilder.toString()));
		}
	}
        public void setFileTag(String tag)
        {
                file_tag = tag;
        }
        public void setSeparator(String tag)
        {
                separator = tag;
        }
        public void setCommonSeparator(String tag)
        {
                commonSeparator = tag;
        }

}
