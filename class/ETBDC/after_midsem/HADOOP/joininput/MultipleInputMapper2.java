import java.io.IOException;
import org.apache.hadoop.conf.Configuration;
import org.apache.hadoop.io.LongWritable;
import org.apache.hadoop.io.Text;
import org.apache.hadoop.mapreduce.Mapper;
public class MultipleInputMapper2 extends MultipleInputMapper
{
	private static String separator;
	private static String commonSeparator;
	private static String FILE_TAG="F2";
	public void setup(Context context)
	{
		Configuration configuration = context.getConfiguration();
		//Retrieving the file separator from context for file2.
		separator = configuration.get("Separator.File2");
		//Retrieving the file separator from context for writing the data to reducer.
		commonSeparator=configuration.get("Separator.Common");
		super.setFileTag(FILE_TAG);
                super.setSeparator(separator);
                super.setCommonSeparator(commonSeparator);
	}
}
