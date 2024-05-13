import java.io.IOException;
import org.apache.hadoop.conf.Configuration;
import org.apache.hadoop.io.LongWritable;
import org.apache.hadoop.io.Text;
import org.apache.hadoop.mapreduce.Mapper;
public class MultipleInputMapper1 extends MultipleInputMapper
{
	private static String separator;
	private static String commonSeparator;
	private static String FILE_TAG="F1";
	public void setup(Context context)
	{
		Configuration configuration = context.getConfiguration();
		//Retrieving the file separator from context for file1.
		separator = configuration.get("Separator.File1");

		//Retrieving the file separator from context for writing the data to reducer.
		commonSeparator=configuration.get("Separator.Common");
		super.setFileTag(FILE_TAG);
		super.setSeparator(separator);
		super.setCommonSeparator(commonSeparator);
	}
}
