public class forcolon{
        public static void main(String[] args) throws InterruptedException 
	{

		String[] myArray = { "abc", "def", "ghi" };
  
		//standard for loop, using array indexes...
		for(int x = 0; x < myArray.length; x++) {
  			System.out.println(myArray[x]);
		}
  
		for( String s : myArray ) {
  			System.out.println(s);
		}
	}
}
