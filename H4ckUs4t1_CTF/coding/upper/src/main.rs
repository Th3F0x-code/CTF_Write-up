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
    let random_number = rng.gen_range(0..100);
    let generated_string = create_string(random_number);
    let solution = solv_algorithm(generated_string.clone());

    println!("Input: {}", generated_string);
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
    println!("Input: a----b             Output: A----B\n");
    println!("Input: Hello!!            Output: hELLO!!\n");
    println!("Input: AAbBcc             Output: aaBbCC\n");
    println!("Input: TesT               Output: tESt\n");
    println!("Now it's your turn to try it out!\n");
    println!("Press enter to continue...");
}


fn create_string(random_number: usize) -> String {
    let alphabet = vec!['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i',
                        'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r',
                        's', 't', 'u', 'v', 'w', 'x', 'y', 'z', '-', '!', '?'];

    let mut output = String::new();
    for _ in 0..random_number {
        let random_index = rand::thread_rng().gen_range(0..26);
        let random_letter = alphabet[random_index];
        output.push(random_letter);
    }

    for i in 0..output.len() {
        if rand::thread_rng().gen_range(0..2) == 1 {
            output.replace_range(i..i + 1, &output[i..i + 1].to_uppercase());
        }
    }


    return output;
}

fn solv_algorithm(input: String) -> String {
    let mut output = String::new();
    for c in input.chars() {
        if c.is_lowercase() {
            output.push(c.to_uppercase().to_string().chars().next().unwrap());
        } else {
            output.push(c.to_lowercase().to_string().chars().next().unwrap());
        }
    }

    return output;
}