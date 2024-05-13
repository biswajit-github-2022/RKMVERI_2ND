package SalesCountry;

import java.io.BufferedReader;
import org.apache.hadoop.mapreduce.RecordReader;
import org.apache.hadoop.io.Text;
import org.apache.hadoop.io.LongWritable;
import java.io.IOException;
import java.io.InputStreamReader;
import org.apache.hadoop.mapreduce.InputSplit;
import org.apache.hadoop.mapreduce.TaskAttemptContext;
import org.apache.hadoop.mapreduce.lib.input.FileSplit;
import org.apache.hadoop.conf.Configuration;
import org.apache.hadoop.fs.FSDataInputStream;
import org.apache.hadoop.fs.FileSystem;

/**
 *
 * @author kamal
 */
class CustomRecordReader extends RecordReader<LongWritable, Text> {

    private LongWritable key;
    private Text value;
    private FileSplit fsplit;
    private Configuration conf;
    private FSDataInputStream fsinstream;
    private FileSystem fs;
    private long splitstart = 0;
    private long splitlen = 0;
    private long bytesread = 0;
    private BufferedReader br;
    private final int newlinebytes = ("\n").getBytes().length;

    @Override
    public void initialize(InputSplit split, TaskAttemptContext context)
            throws IOException {

/*  Initialize Input stream and reader. We use stream to seek to start of
    split position and reader to readlines
*/
	    System.out.println("Initialize called");

        this.fsplit = (FileSplit) split;
        this.conf = context.getConfiguration();

        fs = fsplit.getPath().getFileSystem(conf);
        fsinstream = fs.open(fsplit.getPath());
        br = new BufferedReader(new InputStreamReader(fsinstream));

//  Initialize split start and split length

        splitstart = fsplit.getStart();
        splitlen = fsplit.getLength();

    }

/* Read Nline records till split boundary. NewLine character length is added to 
   overall count of bytes read as it is lost during readline.
*/
    @Override
    public boolean nextKeyValue() throws IOException {
            String line;
            if (bytesread > splitlen)
                    return false;
            if (splitstart != 0)
                    return false;
            if ((line = br.readLine()) != null) {
		System.out.println(line);
                bytesread += (line.getBytes().length + newlinebytes);
                value = new Text(line);
                key = new LongWritable(splitstart);
		br.skip(4);
                return true;
            } else {
                return false;
            }
        }


    @Override
    public void close() throws IOException {
// do nothing
    }

    @Override
    public LongWritable getCurrentKey() {
        return this.key;
    }

    @Override
    public Text getCurrentValue() {
        return this.value;
    }

    @Override
    public float getProgress() throws IOException {
        return true ? 1.0f : 0.0f;
    }
}

