// Java program to demonstrate
// Optional.orElse() method

import java.util.*;

public class opt_null {

	public static void main(String[] args)
	{

		// create a Optional
		Optional<Integer> op
			= Optional.empty();

		// print value
		System.out.println("Optional: "
						+ op);

		try {

			// orElse value
			System.out.println("Value by orElse"
							+ "(100) method: "
							+ op.orElse(100));
		}
		catch (Exception e) {
			System.out.println(e);
		}
	}
}

