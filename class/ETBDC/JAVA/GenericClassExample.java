// Generic class named Box
class Box<T> {
    private T content;

    // Constructor
    public Box(T content) {
        this.content = content;
    }

    // Getter method for content
    public T getContent() {
        return content;
    }

    // Setter method for content
    public void setContent(T content) {
        this.content = content;
    }

    // Method to display information about the content
    public void displayInfo() {
        System.out.println("Box contains: " + content);
    }
}

// Main class to demonstrate the generic class
public class GenericClassExample {
    public static void main(String[] args) {
        // Creating a Box of Integer
        Box<Integer> intBox = new Box<>(10);
        intBox.displayInfo();

        // Creating a Box of String
        Box<String> strBox = new Box<>("Hello, Generics!");
        strBox.displayInfo();

        // Creating a Box of Double
        Box<Double> doubleBox = new Box<>(3.14);
        doubleBox.displayInfo();
    }
}
