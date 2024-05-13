package word_count_DC;



import java.io.*;
import java.util.*;
import java.net.URI;

import org.apache.hadoop.io.Text;
import org.apache.hadoop.io.LongWritable;
import org.apache.hadoop.mapreduce.Mapper;
import org.apache.hadoop.fs.FileSystem;
import org.apache.hadoop.fs.Path;

public class Cached_Word_Count extends Mapper<LongWritable,Text,Text,LongWritable> {

	ArrayList<String> stopWords = null;
	
	
	
	public void setup(Context context)throws IOException,InterruptedException
	{ 
		stopWords = new ArrayList<String>();
		
		URI []cacheFiles = context.getCacheFiles();
		
		if(cacheFiles!=null && cacheFiles.length>0)
		{
			try
			{
				String line ="";
				/*  Create a FileSystem object and pass configuration object in it.
					FileSystem is an abstract base class for a fairly generic filesystem.
					All user code that may potentially use the Hadoop Distributed File System 
					         should be written to use a FileSystem object.
				*/
				FileSystem fs = FileSystem.get(context.getConfiguration());
				Path getFilePath = new Path(cacheFiles[0].toString());  
				
				/*
				We open the file using FileSystem object, convert the input byte stream to 
				character streams using InputStreamReader 
				and wrap it in BufferedReader to make it more efficient
				*/
				BufferedReader reader = new BufferedReader(new InputStreamReader(fs.open(getFilePath)));
				
				while((line = reader.readLine())!=null)
				{
					String []words = line.split(" ");
					
					for(int i=0;i<words.length;i++)
					{
						stopWords.add(words[i]); //add the words to ArrayList
					}
						
				}
			
				
			}catch(Exception e) {
				System.out.println("Unable to read the file");
				System.exit(1);
			}
		}
		
	}	
	
	
	public void map(LongWritable key,Text value, Context context)throws IOException,InterruptedException
	{
		String words[] = value.toString().split(" ");

		for(int i=0;i<words.length;i++) {
		
			//removing all special symbols and converting it to lowerCase
			String temp = words[i].replaceAll("[?,'()]","").toLowerCase();
			
			//if not present in ArrayList we write
			  if(!stopWords.contains(temp))
		     { 
		    	 context.write(new Text(temp),new LongWritable(1));
	
		     }
		}
	}
	
	
	
	
}
