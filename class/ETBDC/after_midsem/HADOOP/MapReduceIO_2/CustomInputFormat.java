package SalesCountry;


import org.apache.hadoop.mapreduce.lib.input.FileInputFormat;
import org.apache.hadoop.mapreduce.RecordReader;
import org.apache.hadoop.io.Text;
import org.apache.hadoop.mapreduce.InputSplit;
import org.apache.hadoop.mapreduce.TaskAttemptContext;
import org.apache.hadoop.io.LongWritable;
import java.io.IOException;

/**
 *
 * @author kamal
 * Class does nothing except returning our customized record reader.
 */

public class CustomInputFormat extends FileInputFormat {


    @Override
    public RecordReader<LongWritable, Text> createRecordReader(InputSplit split,
            TaskAttemptContext context) throws IOException {
        CustomRecordReader reader = new CustomRecordReader();
        return reader;
    }

}

