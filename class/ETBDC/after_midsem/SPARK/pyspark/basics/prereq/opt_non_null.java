// Java program to demonstrate
// Optional.orElse() method

import java.util.*;

public class opt_non_null {

	public static void main(String[] args)
	{

		// create a Optional
		Optional<Integer> op
			= Optional.of(9455);

		// print value
		System.out.println("Optional: "
						+ op);

		// orElse value
		System.out.println("Value by orElse"
						+ "(100) method: "
						+ op.orElse(100));
	}
}

