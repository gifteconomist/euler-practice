fn main() {
    let ceiling = 1000;
    let mut sum = 0;
    for i in 0..ceiling {
      if is_mod_3_or_5(i) {
        sum = sum + i;
      }
    }
    return println!("{0}", sum);
}

fn is_mod_3_or_5(num: u32) -> bool {
    return num % 3 == 0 || num % 5 == 0;
}