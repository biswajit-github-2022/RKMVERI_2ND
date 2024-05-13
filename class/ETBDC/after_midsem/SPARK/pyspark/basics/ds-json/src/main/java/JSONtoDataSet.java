import java.io.Serializable;
 
import org.apache.spark.sql.Dataset;
import org.apache.spark.sql.Encoder;
import org.apache.spark.sql.Encoders;
import org.apache.spark.sql.SparkSession;
 
public class JSONtoDataSet {
 
    public static class Employee implements Serializable{
        public String name;
        public int salary;
    }
 
    public static void main(String[] args) {
        // configure spark
        SparkSession spark = SparkSession
                .builder()
                .appName("Read JSON File to DataSet")
                .master("local[2]")
                .getOrCreate();
 
        // Java Bean (data class) used to apply schema to JSON data
        Encoder<Employee> employeeEncoder = Encoders.bean(Employee.class);
 
        String jsonPath = "data/employees.json";
 
        // read JSON file to Dataset
        Dataset<Employee> ds = spark.read().json(jsonPath).as(employeeEncoder);
        ds.show();
    }
}
