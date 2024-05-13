// Java program to iterate over an ArrayList
// Using Iterator

// Importing all utility classes
import java.util.*;

// Main class
class lists {

	// Main driver method
	public static void main(String[] args)
	{
		// Declaring and initializing ArrayList
		List<Integer> numbers
			= Arrays.asList(1, 2, 3, 4, 5, 6, 7, 8);

		// Iterating ArrayList using Iterator
		Iterator it = numbers.iterator();

		// Holds true till there is single element
		// remaining in the list
		while (it.hasNext())

			// Print the elements of ArrayList
			System.out.print(it.next() + " ");
	}
}

