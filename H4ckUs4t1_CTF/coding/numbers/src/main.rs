use std::io;
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
    let random_number = rng.gen_range(1..15);

    let solution = solution(random_number);

    println!("Input: {} ", random_number);
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
    println!("Input: 1             Output: 1\n");
    println!("Input: 3             Output: 123123123\n");
    println!("Input: 10            Output: 1234512345123451234512345\n");
    println!("Input: 10            Output: 12345678910123456789101234567891012345678910123456789101234567891012345678910123456789101234567891012345678910\n");
    println!("Now it's your turn to try it out!\n");
    println!("Press enter to continue...");
}


fn solution(number: usize) -> String {
    let mut solution = String::new();
    let numbers = vec!["0", "1", "2", "3", "4", "5", "6", "7", "8", "9", "10", "11", "12", "13", "14", "15", "16", "17", "18", "19", "20"];
    for i in 0..number {
        solution.push_str(numbers[i + 1]);
    }
    return solution.repeat(number);
}