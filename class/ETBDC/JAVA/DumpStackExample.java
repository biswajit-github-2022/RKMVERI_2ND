public class DumpStackExample extends Thread {
    public static void main(String[] args) {
            functionA(5);
    }

    public static void functionA(int n) {
         Thread.currentThread().dumpStack();
    }

}