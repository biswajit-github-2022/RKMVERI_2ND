import java.io.IOException;
import java.util.Arrays;
import org.apache.hadoop.conf.Configuration;
import org.apache.hadoop.io.LongWritable;
import org.apache.hadoop.io.Text;
import org.apache.hadoop.mapreduce.Reducer;
public class MultipleInputReducer extends Reducer<LongWritable, Text, LongWritable, Text>
{
private static String commonSeparator;
public void setup(Context context)
{
Configuration configuration = context.getConfiguration();
//Retrieving the common file separator from context for output file.
commonSeparator=configuration.get("Separator.Common");
}

@Override
public void reduce(LongWritable key, Iterable<Text>
textValues, Context context) throws IOException, InterruptedException
{
StringBuilder stringBuilder = new StringBuilder();
String[] firstFileValues=null, secondFileValues=null;
String[] stringValues;
for (Text textValue : textValues)
{
stringValues = textValue.toString().split(commonSeparator);
if("F1".equalsIgnoreCase(stringValues[0]))
{
//				firstFileValues = stringValues;
firstFileValues=Arrays.copyOf(stringValues, stringValues.length);
}
if("F2".equalsIgnoreCase(stringValues[0]))
{
secondFileValues = Arrays.copyOf(stringValues, stringValues.length);
}
}
if(firstFileValues != null)
{
for(int index=1;index<firstFileValues.length;index++)
{
stringBuilder.append(firstFileValues[index]+commonSeparator);
}
}
if(secondFileValues != null)
{
for(int index=1;index<secondFileValues.length;index++)
{
stringBuilder.append(secondFileValues[index]+commonSeparator);
}
}
context.write(key, new Text(stringBuilder.toString()));
}
}
