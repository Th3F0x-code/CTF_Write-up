use std::fs::File;
use std::io::Read;
use text_io::read;


fn gen(n: i32) -> Vec<i128> {
    let mut primo: i128 = 0;
    let mut secondo: i128 = 1;
    let mut terzo: i128;
    let mut vec: Vec<i128> = Vec::new();

    for _i in 0..n {
        terzo = primo + secondo;
        primo = secondo;
        secondo = terzo;
        vec.push(terzo);
    }
    vec
}

fn main() {
    println!("Welcome to this new challenge");
    println!("do u know the fibonacci sequence?");
    println!("if u do, u can solve this challenge");
    println!("if u don't, u can still solve this challenge");
    println!("u can find the fibonacci sequence here: https://en.wikipedia.org/wiki/Fibonacci_number");
    let mut input: i128 = 0;
    let mut i: i128 = 1;
    let mut fib: Vec<i128> = Vec::new();
    fib = gen(100);

    println!("now u have to send me the first 100 numbers of the fibonacci sequence");
    println!("n1 = 1, n2 = 1");
    loop {
        print!("n: ");
        input = read!();
        if input == fib[i as usize] {
            println!("correct");
            i += 1;
        } else {
            println!("incorrect");
            println!("the correct number was {}", fib[i as usize]);
            break;
        }
        if i == 100 {
            let mut file = File::open("flag.txt").unwrap();
            let mut contents = String::new();
            file.read_to_string(&mut contents).expect("flag file not found");
            println!("congrats! u found the flag, what r u waiting for for submit it??");
            println!("{}", contents.trim());
            break;
        }
    }
}


