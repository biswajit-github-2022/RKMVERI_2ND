import java.io.IOException;
import org.apache.hadoop.io.Text;
import org.apache.hadoop.mapreduce.Reducer;

public class MaxSalaryReducer extends Reducer<Text, Text, Text, Text> {

    @Override
    protected void reduce(Text key, Iterable<Text> values, Context context) throws IOException, InterruptedException {
        try {
            int maxSalary = Integer.MIN_VALUE;

            // Iterate through all salary values and find the maximum
            for (Text value : values) {
                int currentSalary = Integer.parseInt(value.toString());
                if (currentSalary > maxSalary) {
                    maxSalary = currentSalary;
                }
            }

            // Emit department and corresponding maximum salary
            context.write(key, new Text(Integer.toString(maxSalary)));
        } catch (Exception e) {
            // Handle exceptions (if any)
            System.err.println("Error in Reducer: " + e.getMessage());
        }
    }
}

