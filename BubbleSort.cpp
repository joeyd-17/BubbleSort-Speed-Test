#include <ctime>
#include <fstream>
#include <iostream>
#include <string>
#include <vector>
using namespace std;

int main(int argc, char* argv[]) {
    int size;
    // Get command line input
    if (argc > 1) {
        size = stoi(argv[1]);
    } else {
        size = 10000;
    }
    cout << "Looking for size: " << size << endl;
    
    //Declare a vector of longs to store the numbers
    vector<long> numbers;
    
    //Read size numbers from numbers.txt
    ifstream file("numbers.txt");
    long line;

    for(int i = 0; i < size; i++)
    {
        file >> line;
        numbers.push_back(line);
    }

    file.close();
    
    //Print the vector size (to make sure it matches the size printed above)
    cout << "Size: " << numbers.size() << endl;

    //Bubble Sort the vector
    bool swapped = true;
    int index = numbers.size() - 1;
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
    cout << "The first 10 numbers:" << endl;
    for(int i = 0; i < 10; i++){
        cout << numbers[i] << " ";
    }

    cout << endl << "The last 10 numbers:" << endl;
    for(int i = numbers.size() - 10; i < numbers.size(); i++){
        cout << numbers[i] << " ";
    }

    return 0;
}
