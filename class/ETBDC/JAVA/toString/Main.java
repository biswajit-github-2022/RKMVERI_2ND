class ToString {
    private int id;
    private String name;

    // Constructor
    public ToString() {
        // Constructor code here, if needed
    }

    // Getter and setter methods for id
    public int getId() {
        return id;
    }

    public void setId(int id) {
        this.id = id;
    }

    // Getter and setter methods for name
    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }

    @Override
    public String toString() {
        return "ToString{id=" + id + ", name='" + name + "'}";
    }
}

public class Main {
    public static void main(String[] args) {
        // Create an instance of ToString class
        ToString obj = new ToString();
        
        // Set values for id and name using setters
        obj.setId(1);
        obj.setName("John Doe");
        
        // Print the object using toString()
        System.out.println("Using toString(): " + obj.toString());

        // Implicit call to toString() when concatenating with a string
        System.out.println("Implicit toString(): " + obj);
    }
}