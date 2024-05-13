import java.io.IOException;
import org.apache.hadoop.io.LongWritable;
import org.apache.hadoop.io.Text;
import org.apache.hadoop.mapreduce.Mapper;

public class MaxSalaryMapper extends Mapper<LongWritable, Text, Text, Text> {

    private Text department = new Text();
    private Text salary = new Text();

    // Enum for counters
    enum Sales {
        INVALID_SALARY
    }

    @Override
    protected void map(LongWritable key, Text value, Context context) throws IOException, InterruptedException {
        try {
            // Split the input line by ","
            String[] fields = value.toString().split(",");

            // Extract department and salary information
            String dept = fields[3].trim();
            String sal = fields[4].trim();

            // Check if salary is a valid integer
            if (isValidInteger(sal)) {
                // Set department as the key and salary as the value
                department.set(dept);
                salary.set(sal);
                // Emit key-value pair
                context.write(department, salary);
            } else {
                // Increment the INVALID_SALARY counter
                context.getCounter(Sales.INVALID_SALARY).increment(1);
            }
        } catch (Exception e) {
            // Handle exceptions (if any)
            System.err.println("Error in Mapper: " + e.getMessage());
            context.getCounter(Sales.INVALID_SALARY).increment(1);
            return;
        }
    }

    // Helper method to check if a string can be parsed as an integer
    private boolean isValidInteger(String str) {
        try {
            Integer.parseInt(str);
            return true;
        } catch (NumberFormatException e) {
            return false;
        }
    }
}

