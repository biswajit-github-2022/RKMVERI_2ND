package SalesCountry;

import java.io.IOException;

import org.apache.hadoop.io.IntWritable;
import org.apache.hadoop.io.LongWritable;
import org.apache.hadoop.io.Text;
import org.apache.hadoop.mapred.*;
import org.apache.hadoop.mapreduce.Job;
import org.apache.hadoop.mapreduce.Mapper;
import org.apache.hadoop.mapreduce.Reducer;

import java.lang.*;

public class SalesMapper extends Mapper<LongWritable, Text, LongWritable, Text> {
	private final static IntWritable one = new IntWritable(1);

	enum Sales {
		SALES_DATA_MISSING,
		SALES_DATA_HEADER
	};


	public void map(LongWritable key, Text value, Context context) throws IOException, InterruptedException {

		String valueString = value.toString();
		String[] SingleCountryData = valueString.split(",");
		String cell = SingleCountryData[2];
		if (cell.compareTo("Price") == 0) {
			context.getCounter(Sales.SALES_DATA_HEADER).increment(1);
			return;
		}
		int price = 0;
		try {
			price = Integer.parseInt(cell);
			price = (-1) * price;
		} catch (final NumberFormatException e) {
			context.getCounter(Sales.SALES_DATA_MISSING).increment(1);
			return;
		}
		//if (7500 == price) // Returns 0 because they are equal
			context.write(new LongWritable(price), new Text(SingleCountryData[7]));
		//output.collect(new Text("test"), one);
	}
}
