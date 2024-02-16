// Define an enum called DayOfWeek
enum DayOfWeek {
    SUNDAY,
    MONDAY,
    TUESDAY,
    WEDNESDAY,
    THURSDAY,
    FRIDAY,
    SATURDAY
}

public class EnumExample {
    public static void main(String[] args) {
        // Accessing enum constants
        DayOfWeek today = DayOfWeek.TUESDAY;

        // Switch statement with enum
        switch (today) {
            case MONDAY:
                System.out.println("Today is Monday");
                break;
            case TUESDAY:
                System.out.println("Today is Tuesday");
                break;
            case WEDNESDAY:
                System.out.println("Today is Wednesday");
                break;
            case THURSDAY:
                System.out.println("Today is Thursday");
                break;
            case FRIDAY:
                System.out.println("Today is Friday");
                break;
            case SATURDAY:
                System.out.println("Today is Saturday");
                break;
            case SUNDAY:
                System.out.println("Today is Sunday");
                break;
            default:
                System.out.println("Invalid day");
        }

        // Iterating over enum constants
        System.out.println("Days of the week:");
        for (DayOfWeek day : DayOfWeek.values()) {
            System.out.println(day);
        }
    }
}