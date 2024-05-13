import org.apache.hadoop.conf.Configuration;
import org.apache.hadoop.fs.Path;
import org.apache.hadoop.io.Text;
import org.apache.hadoop.mapreduce.Job;
import org.apache.hadoop.mapreduce.lib.input.TextInputFormat;
import org.apache.hadoop.mapreduce.lib.output.TextOutputFormat;
import org.apache.hadoop.util.Tool;
import org.apache.hadoop.util.ToolRunner;

public class MaxSalaryDriver implements Tool {

    private Configuration configuration;

    @Override
    public int run(String[] args) throws Exception {
        Job job = Job.getInstance(getConf(), "MaxSalaryJob");
        job.setJarByClass(getClass());

        // Set input and output paths
        TextInputFormat.addInputPath(job, new Path(args[0]));
        TextOutputFormat.setOutputPath(job, new Path(args[1]));

        // Set mapper, reducer, and combiner classes
        job.setMapperClass(MaxSalaryMapper.class);
        job.setReducerClass(MaxSalaryReducer.class);

        // Set input and output key-value classes
        job.setOutputKeyClass(Text.class);
        job.setOutputValueClass(Text.class);

        // Wait for the job to complete
        return job.waitForCompletion(true) ? 0 : 1;
    }

    @Override
    public Configuration getConf() {
        return configuration;
    }

    @Override
    public void setConf(Configuration configuration) {
        this.configuration = configuration;
    }

    public static void main(String[] args) throws Exception {
        int exitCode = ToolRunner.run(new MaxSalaryDriver(), args);
        System.exit(exitCode);
    }
}

