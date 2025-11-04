//Bubble Sort
import java.io.*;
import java.util.*;


public class BubbleSort {


    public static void main(String[] args) throws FileNotFoundException {
        int size;
        if (args.length > 0) {
            size = Integer.parseInt(args[0]);
        } else {
            size = 10000;
        }
        System.out.println("Looking for size: " + size + "!");
        Vector<Long> numbers = new Vector<>();
        //Declare a vector of longs to store the numbers

        long line;

        //Read size numbers from numbers.txt
        Scanner reader = new Scanner(new File("numbers.txt"));

        for (int i = 0; i < size; i++) {
            line = reader.nextLong();
            numbers.add(line);
        }

        //Print the vector size (to make sure it matches the size printed above)
        System.out.println("Size: " + numbers.size());


        //Bubble Sort
        boolean swapped = true;
        int index = numbers.size() - 1;
        while (swapped) {
            swapped = false;
            for (int i = 0; i < index; i++) {
                if (numbers.get(i) > numbers.get(i + 1)) {
                    long number = numbers.get(i);
                    numbers.set(i, numbers.get(i + 1));
                    numbers.set(i + 1, number);
                    swapped = true;
                }
            }
            --index;
        }


        //Print the first and last ten numbers from the vector to the console
        System.out.print("The first 10 numbers: ");
        for (int i = 0; i < 10; i++) {
            System.out.print(numbers.get(i) + " ");
        }

        System.out.print("The last 10 numbers: ");
        for (int i = numbers.size() - 10; i < numbers.size(); i++) {
            System.out.print(numbers.get(i) + " ");
        }

    }
}

      
   
   