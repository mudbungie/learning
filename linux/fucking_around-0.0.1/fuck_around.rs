use std::thread::sleep;
use std::time::Duration;

fn main() {
    println!("service started");
    let uptime = Duration::from_secs(1);
    sleep(uptime);
    println!("service exited")
}
