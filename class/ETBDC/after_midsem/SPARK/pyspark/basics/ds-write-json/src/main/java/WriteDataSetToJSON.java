import java.io.Serializable;
 
import org.apache.spark.sql.Dataset;
import org.apache.spark.sql.Encoder;
import org.apache.spark.sql.Encoders;
import org.apache.spark.sql.SparkSession;
 
public class WriteDataSetToJSON {
    public static class Employee implements Serializable{
        public String name;
        public int salary;
    }
 
    public static void main(String[] args) {
        // configure spark
        SparkSession spark = SparkSession
                .builder()
                .appName("Spark Example - Write Dataset to JSON File")
                .master("local[2]")
                .getOrCreate();
 
        Encoder<Employee> employeeEncoder = Encoders.bean(Employee.class);
        String jsonPath = "data/employees.json";
        Dataset<Employee> ds = spark.read().json(jsonPath).as(employeeEncoder);
         
        // write dataset to JSON file
        ds.write().json("data/out_employees/");
    }
}
