public class ExceptionHandlingExample {
    public static void main(String[] args) {
        try {
            // Some code that may throw an exception
            int result = divide(10, 0);
            System.out.println("Result: " + result); // This line will not execute if an exception occurs
        } catch (ArithmeticException e) {
            // Catching specific type of exception
            System.err.println("Error: Division by zero");
            e.printStackTrace();
        } catch (Exception e) {
            // Catching any other type of exception
            System.err.println("Error: Something went wrong");
            e.printStackTrace();
        } finally {
            // Code in finally block always executes, regardless of whether an exception occurred
            System.out.println("Finally block executed");
        }
    }

    public static int divide(int dividend, int divisor) {
        // Method that may throw an exception
        return dividend / divisor;
    }
}