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
    let random_number = rng.gen_range(1..100000);
    let generated_string = create_string(random_number);

    println!("Input: {}", random_number);
    println!("{}", create_string(random_number));

    let input: String;
    print!("Output: ");
    input = read!("{}\n");

    return if input == generated_string {
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
    println!("Input: 1                Output: 1 2 3 4 5 6 7 8 9 10\n");
    println!("Input: 21               Output: 21 42 63 84 105 126 147 168 189 210\n");
    println!("Input: 8992             Output: 8992 17984 26976 35968 44960 53952 62944 71936 80928 89920\n");
    println!("Input: 20001            Output: 20001 40002 60003 80004 100005 120006 140007 160008 180009 200010\n");
    println!("Now it's your turn to try it out!\n");
    println!("Press enter to continue...");
}


fn create_string(random_number: usize) -> String {
    let mut output = String::new();
    let mut i = 1;
    while i <= 10 {
        output.push_str(&(random_number * i).to_string());
        output.push_str(" ");
        i += 1;
    }

    return output;
}

