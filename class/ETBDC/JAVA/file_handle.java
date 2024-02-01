import java.io.BufferedReader;
import java.io.FileReader;
import java.io.IOException;

public class file_handle {

    public static void main(String[] args) {
        String csvFile = "ODI_data.csv";

        try (BufferedReader br = new BufferedReader(new FileReader(csvFile))) {
            String line;
            int column_number=3;
            while ((line = br.readLine()) != null) {
                // Split the CSV line into an array of values based on the comma
                String[] values = line.split(",");
                // System.out.println(Arrays.toString(values));
                // Process the values as needed
                // for (String value : values) {
                //     System.out.print(value + " ");
                // }
                // System.out.println(); // Move to the next line for the next row
                System.out.println(values[column_number]);
            }
        } catch (IOException e) {
            e.printStackTrace();
        }
    }
}
