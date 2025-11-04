#include <stdio.h>
#include <stdbool.h>
#include <stdlib.h>

int main(int argc, char* argv[]) {
    int size;
    // Get command line input
    if (argc > 1) {
        size = atoi(argv[1]);
    } else {
        size = 10000;
    }

    printf("Looking for size %d\n", size);
    
    //Declare a vector of longs to store the numbers
    long numbers[size];
    
    //Read size numbers from numbers.txt
    FILE *fptr;
    fptr = fopen("numbers.txt", "r");

    long line;

    for(int i = 0; i < size; i++)
    {
        fscanf(fptr, "%ld", &line);
        numbers[i] = line;
    }

    fclose(fptr);
    
    //Print the vector size (to make sure it matches the size printed above)
    int numbersSize = sizeof(numbers) / sizeof(numbers[0]);
    printf("Vector size %d\n", numbersSize);

    //Bubble Sort the vector
    bool swapped = true;
    int index = numbersSize - 1;
    while(swapped){
        swapped = false;
    
        for(int i = 0; i < index; i++){
            if(numbers[i + 1] < numbers[i]){
                long number = numbers[i];
                numbers[i] = numbers[i + 1];
                numbers[i + 1] = number;
                swapped = true;
            }
        }

        --index;
    }
    
    //Print the first and last ten numbers from the vector to the console
    printf("The first 10 numbers\n");
    for(int i = 0; i < 10; i++){
        printf("%ld ", numbers[i]);
    }

    printf("The last 10 numbers\n");
    for(int i = numbersSize - 10; i < numbersSize; i++){
        printf("%ld ", numbers[i]);
    }

    printf("\n");

    return 0;
}