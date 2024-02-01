// Define an interface named Shape
interface Shape {
    // Abstract method to calculate area
    double calculateArea();

    // Abstract method to display shape information
    void display();
}

// Implementing the interface in a class
class Circle implements Shape {
    private double radius;

    // Constructor
    public Circle(double radius) {
        this.radius = radius;
    }

    // Implementing calculateArea method for Circle
    @Override
    public double calculateArea() {
        return Math.PI * radius * radius;
    }

    // Implementing display method for Circle
    @Override
    public void display() {
        System.out.println("Circle with radius: " + radius);
    }
}

// Another class implementing the interface
class Rectangle implements Shape {
    private double length;
    private double width;

    // Constructor
    public Rectangle(double length, double width) {
        this.length = length;
        this.width = width;
    }

    // Implementing calculateArea method for Rectangle
    @Override
    public double calculateArea() {
        return length * width;
    }

    // Implementing display method for Rectangle
    @Override
    public void display() {
        System.out.println("Rectangle with length " + length + " and width " + width);
    }
}

// Main class to demonstrate the interface
public class InterfaceExample {
    public static void main(String[] args) {
        // Creating objects of Circle and Rectangle
        Circle circle = new Circle(5);
        Rectangle rectangle = new Rectangle(4, 6);

        // Using the interface methods
        circle.display();
        System.out.println("Area of Circle: " + circle.calculateArea());

        rectangle.display();
        System.out.println("Area of Rectangle: " + rectangle.calculateArea());
    }
}
