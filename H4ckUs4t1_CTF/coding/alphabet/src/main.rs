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
    let solution = algorithm(random_number);

    println!("Input: {}", random_number + 1);
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
    println!("Input: 5             Output: EEEEE\n");
    println!("Input: 17            Output: QQQQQQQQQQQQQQQQQ\n");
    println!("Input: 1             Output: A\n");
    println!("Input: 3             Output: CCC\n");
    println!("Input: 25            Output: YYYYYYYYYYYYYYYYYYYYYYYYY\n");
    println!("Now it's your turn to try it out!\n");
    println!("Press enter to continue...");
}


fn algorithm(random_number: usize) -> String {
    let alphabet = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I',
        'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R',
        'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'];

    let mut output = String::new();
    for _ in 0..random_number + 1 {
        output.push(alphabet[random_number]);
    }
    return output;
}