public class CompareToExample {
    public static void main(String[] args) {
        String str1 = "apple";
        String str2 = "banana";
        String str3 = new String("apple");

        int result = str1.compareTo(str2);

        if (result < 0) {
            System.out.println("str1 is less than str2");
        } else if (result > 0) {
            System.out.println("str1 is greater than str2");
        } else {
            System.out.println("str1 is equal to str2");
        }
        result = str1.compareTo(str3);
        if (result < 0) {
            System.out.println("str1 is less than str3");
        } else if (result > 0) {
            System.out.println("str1 is greater than str3");
        } else {
            System.out.println("str1 is equal to str3");
        }
    }

}