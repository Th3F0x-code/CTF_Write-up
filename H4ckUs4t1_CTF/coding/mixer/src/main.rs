use std::io;
use rand::prelude::SliceRandom;
use rand::Rng;
use text_io::read;

fn main() {
    tutorial();
    wait_for_enter();
    for _ in 0..1000 {
        if !run() {
            println!("Wrong answer!");
            return;
        }
    }
    win();
    return;
}

fn win() {
    let contents = std::fs::read_to_string("./src/flag.txt")
        .expect("Something went wrong reading the file");
    println!("The flag is: {}", contents);
}

fn run() -> bool {
    let mut rng = rand::thread_rng();
    let random_number = rng.gen_range(1..26);
    let string = generate_string(random_number);
    let numbers = generate_numbers(random_number);
    let solution = generate_solution(string.clone(), numbers.clone());
    println!("Input: {} | {} | {}", random_number, string, numbers);
    let input: String;
    print!("Output: ");
    input = read!("{}\n");

    return if input.trim() == solution {
        true
    } else {
        false
    };
}

fn wait_for_enter() {
    let mut input = String::new();
    io::stdin().read_line(&mut input).expect("Failed to read line");
}

fn tutorial() {
    println!("Try to guess what this program does.");
    println!("Input: 4 | abcd | 4 3 2 1                         Output: dcba\n");
    println!("Input: 6 | abcdef | 1 6 2 5 3 4                   Output: afbecd\n");
    println!("Input: 8 | abcd1234 | 5 1 6 2 7 3 8 4             Output: 1a2b3c4d\n");
    println!("Input: 1 | a | 1                                  Output: a\n");
    println!("Input: 9 | deellnow_ | 8 3 5 4 9 1 7 6 2          Output: well_done\n");
    println!("Now it's your turn to try it out!\n");
    println!("Press enter to continue...");
}


fn generate_string(random_number: usize) -> String {
    let alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i',
        'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r',
        's', 't', 'u', 'v', 'w', 'x', 'y', 'z', '_', '1', '2', '3', '4', '5', '6', '7', '8', '9', '0', '!', '@', '#'];

    let mut output = String::new();
    for _ in 0..random_number {
        let random_index = rand::thread_rng().gen_range(0..alphabet.len());
        output.push(alphabet[random_index]);
    }

    return output;
}

fn generate_numbers(random_number: usize) -> String {
    let mut output = String::new();
    let mut numbers: Vec<usize> = (1..random_number + 1).collect();
    numbers.shuffle(&mut rand::thread_rng());
    for i in numbers {
        output.push_str(&i.to_string());
        output.push(' ');
    }

    return output;
}

fn generate_solution(string: String, numbers: String) -> String {
    let mut output = String::new();
    let numbers = numbers.trim().split(' ');
    if numbers.clone().count() != string.len() {
        return String::from("Wrong input!");
    }
    for i in numbers {
        let index = i.parse::<usize>().unwrap();
        output.push(string.chars().nth(index - 1).unwrap());
    }
    return output;
}