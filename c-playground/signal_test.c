#include <assert.h>
#include <errno.h>
#include <stdio.h>
#include <stdlib.h>
#include <sys/wait.h>
#include <unistd.h>

int main() {
    // Ignoring SIGCHLD causes waitpid to always return -1 and set errno to
    // ECHILD.
    // See "Consequences of Program Termination" in POSIX
    // http://pubs.opengroup.org/onlinepubs/9699919799/
    signal(SIGCHLD, SIG_IGN);

    int status;
    const pid_t pid = waitpid(WAIT_ANY, &status, WUNTRACED);
    assert(pid == -1);
    assert(errno == ECHILD);
}

void spawn_child() {
    const pid_t fork_result = fork();
    if (fork_result == 0) {
        // This is the child process
        char* const argv[] = { "ls" };
        execvp(argv[0], argv);
    } else if (fork_result < 0) {
        // The fork failed
        perror("fork");
        exit(1);
    } else {
        // This is the parent process
        // nothing to do here
    }
}
