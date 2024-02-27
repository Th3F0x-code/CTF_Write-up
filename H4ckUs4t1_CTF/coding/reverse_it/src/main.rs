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
    let random_number = rng.gen_range(0..26);
    let string = gen_string(random_number);

    let solution = solution(random_number, string.clone());

    println!("Input: {} {}", random_number, string);
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
    println!("Input: 1 Short text                            Output: txet trohS\n");
    println!("Input: 0 Another text                          Output: Another text\n");
    println!("Input: 100 Belive in yourself!                 Output: Belive in yourself!\n");
    println!("Input: 101 This is easy!                       Output: !ysae si sihT\n");
    println!("Now it's your turn to try it out!\n");
    println!("Press enter to continue...");
}


fn gen_string(random_number: usize) -> String {
    let alphabet = ['A', 'a', 'B', 'b', 'C', 'c', 'D', 'd', 'E', 'e',
        'F', 'f', 'G', 'g', 'H', 'h', 'I', 'i', 'J',
        'j', 'K', 'k', 'L', 'l', 'M', 'm', 'N', 'n',
        'O', 'o', 'P', 'p', 'Q', 'q', 'R', 'r', 'S',
        's', 'T', 't', 'U', 'u', 'V', 'v', 'W', 'w',
        'X', 'x', 'Y', 'y', 'Z', 'z'];

    let mut output = String::new();

    for _ in 0..random_number {
        let random_letter = alphabet[rand::thread_rng().gen_range(0..26)];
        output.push(random_letter);
    }
    if output.len() == 0 {
        output.push('a');
    }
    return output;
}


fn solution(number: usize, string_2: String) -> String {
    return if number % 2 == 1 {
        string_2.chars().rev().collect::<String>()
    } else {
        string_2
    };
}