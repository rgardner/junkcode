use chrono::{DateTime, Local};

fn main() {
    let local: DateTime<Local> = Local::now();
    let formatted = local.format("%F.%H-%M-%S");
    println!("{}.log", formatted);
}
