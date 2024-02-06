// equalsoperatpor checks object is same or not

public class EqualsOperatorExample {
    public static void main(String[] args) {
        String str1 = "apple";
        String str2 = "apple";
        String str3 = new String("apple");
        String str4 = new String("apple");

        System.out.println(str1 == str2);  // true (both point to the same "apple" object in the String pool)
        System.out.println(str1 == str3);  // false (str1 is referring to a different object than str3)
        System.out.println(str4 == str3);
    }
}