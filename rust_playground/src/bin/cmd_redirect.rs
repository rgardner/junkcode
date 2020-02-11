//! Demonstrates how to redirect stderr in a child process to a file.

#![cfg(unix)]

use std::{
    io::{self, Read, Seek, SeekFrom},
    os::unix::prelude::*,
    process::Command,
};

use nix::unistd;

fn main() -> Result<(), Box<io::Error>> {
    let mut cmd = Command::new("echo");
    let mut tmp_stderr_file = tempfile::tempfile()?;
    cmd.arg("needle").stderr(tmp_stderr_file.try_clone()?);
    unsafe {
        cmd.pre_exec(|| {
            unistd::dup2(2, 1).expect("dup2(2, 1) failed");
            unistd::close(2).expect("close(2) failed");

            Ok(())
        });
    }
    let mut child = cmd.spawn()?;

    assert!(child.wait()?.success());

    let mut contents = String::new();
    tmp_stderr_file.seek(SeekFrom::Start(0))?;
    tmp_stderr_file.read_to_string(&mut contents)?;
    assert_eq!(contents, "needle\n");

    Ok(())
}
