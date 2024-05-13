import java.util.Arrays;
import java.util.List;

import org.apache.log4j.Level;
import org.apache.log4j.Logger;
import org.apache.spark.SparkConf;
import org.apache.spark.api.java.JavaRDD;
import org.apache.spark.api.java.JavaSparkContext;

public class RDDReduceExample {

	public static void main(String[] args) {
		
		// to remove the unwanted loggers from output.
		Logger.getLogger("org.apache").setLevel(Level.WARN);

		// Getting the numbers list.
		List<Integer> numbersList = getSampleData();
		
		// Creating the SparkConf object
		SparkConf sparkConf = new SparkConf().setAppName("Java RDD_Reduce Example").setMaster("local");

		// Creating JavaSprakContext object
		JavaSparkContext sc = new JavaSparkContext(sparkConf);
		
		// Converting List into JavaRDD.
		JavaRDD<Integer> integersRDD =  sc.parallelize(numbersList);
		
		// Getting the sum of all numbers using reduce() method
		Integer sumResult = integersRDD.reduce( (value1, value2) -> value1 + value2);

		// printing the sum
		
		System.out.println("Sum of RDD numbers using reduce() : "+sumResult);
		
		// closing Spark Context
		sc.close();
		
	}

	/**
	 * returns a list of integer numbers
	 * 
	 * @return
	 */
	private static List<Integer> getSampleData() {

		return Arrays.asList(1, 2, 3, 4, 5, 6, 7, 8, 9);

	}

}
