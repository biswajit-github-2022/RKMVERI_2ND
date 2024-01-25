
class Person {
    void name() {
        System.out.println("My good name is Ram");
    }

    void display() {
        System.out.println("I am a good student");
    }

    void save() {
        System.out.println("saving data in person");
    }

};

class student extends Person {
    void name() {
        System.out.println("My good name is Ram");
    }

    void display() {
        System.out.println("I am a good student");
    }

    void save_student_data() {
        System.out.println("saving data in student");
    }
};

class employee extends Person {
    void name() {
        System.out.println("My name is Rajesh chauhan");
    }

    void display() {
        System.out.println("I am not a good employee");
    }

    void save_emp_data() {
        System.out.println("saving data in employee");
    }
};

class inheritance {
    public static void func_name(Person object) {
        object.name();
        object.display();
        object.save();
    }

    public static void main(String[] args) {
        System.out.println("Hello, World!");
        // creating the instace/object of the class
        student s1 = new student();
        employee e1 = new employee();
        // Passing these class objects in common interface function one by one and get
        // output
        func_name(s1);
        func_name(e1);
        s1.save_student_data();
        e1.save_emp_data();
    }
}
