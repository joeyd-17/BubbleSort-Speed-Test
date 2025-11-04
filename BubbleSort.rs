use std::env;
use std::fs::File;
use std::io::{self, BufRead};

fn main(){
    let args: Vec<String> = env::args().collect();
    let size: i32;
    if args.len() > 1 {
        size = args[1].parse().unwrap();
    }
    else {
        size = 10000;
    }

    println!("Looking for size: {s}", s = size);
    let mut numbers: Vec<i64> = Vec::new();

    let file = File::open("numbers.txt").unwrap();
    let reader = io::BufReader::new(file);

    for line in reader.lines().take(size as usize) {
        let line = line.unwrap();
        let num: i64 = line.parse().unwrap();
        numbers.push(num);
    }

    println!("Got size: {s}", s = numbers.len());

    let mut swapped = true;
    let mut index = numbers.len() - 1;

    while swapped{
        swapped = false;

        for i in 0..index {
            if numbers[i + 1] < numbers[i] {
                let number: i64 = numbers[i];
                numbers[i] = numbers[i + 1];
                numbers[i + 1] = number;
                swapped = true;
            }
        }

        index = index - 1;
    }

    let lowerNumbers = &numbers[0..10];
    let upperNumbers = &numbers[(numbers.len() - 10)..numbers.len()];

    println!("First 10: ");
    for num in lowerNumbers {
        print!("{}, ", num);
    }

    println!("Last 10: ");
    for num in upperNumbers {
        print!("{}, ", num);
    }
}
