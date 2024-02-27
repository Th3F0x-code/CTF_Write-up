
fn main() {
    let hash = "4338f927d968732746fc91a14889ae1f";
    let mut found = false;
    let mut count = 0;

    for i in 0..26 {
        for j in 0..26 {
            for k in 0..26 {
                for l in 0..26 {
                    for m in 0..26 {
                        for n in 0..26 {
                            let word = format!(
                                "{}{}{}{}{}{}",
                                (i + 97) as u8 as char,
                                (j + 97) as u8 as char,
                                (k + 97) as u8 as char,
                                (l + 97) as u8 as char,
                                (m + 97) as u8 as char,
                                (n + 97) as u8 as char
                            );

                            count += 1;
                            let aaa = md5::compute(word.as_bytes());
                            let bbb = format!("{:x}", aaa);
                            println!("{}: {}", word, bbb);
                            if bbb == hash {
                                println!("found: {} in {} tries", word, count);
                                found = true;
                                break;
                            }
                        }
                        if found {
                            break;
                        }
                    }
                    if found {
                        break;
                    }
                }
                if found {
                    break;
                }
            }
            if found {
                break;
            }
        }
        if found {
            break;
        }
    }

    if !found {
        println!("Word not found in {} tries", count);
    }
}
