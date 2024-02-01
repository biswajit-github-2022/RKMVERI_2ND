import java.util.Scanner;
class hi {
    public static void main(String[] args) {
        System.out.println("Hello, World!");
        Scanner sc = new Scanner(System.in);
        int number = sc.nextInt();
        System.out.println(number);
        sc.close();
    }
}
// javac -d ../class_file hi.java
// java -cp ../class_file hi 
// jar cf MyApplication.jar -C classes/ .