#include <errno.h>
#include <stdbool.h>
#include <stdio.h>
#include <stdlib.h>
#include <sys/wait.h>
#include <unistd.h>

#include "test_suites.h"

// Ignoring SIGCHLD causes waitpid to always return -1 and set errno to
// ECHILD.
// See "Consequences of Program Termination" in POSIX
// http://pubs.opengroup.org/onlinepubs/9699919799/
START_TEST(signal_waitpid_ignore_child_test) {
  signal(SIGCHLD, SIG_IGN);

  int status;
  const pid_t pid = waitpid(WAIT_ANY, &status, WUNTRACED);
  ck_assert_int_eq(pid, -1);
  ck_assert_int_eq(errno, ECHILD);
}
END_TEST

START_TEST(signal_spawn_child_test) {
  const pid_t fork_result = fork();
  if (fork_result == 0) {
    // This is the child process
    ck_assert(true);
  } else if (fork_result < 0) {
    ck_abort_msg(strerror(errno));
  } else {
    // This is the parent process
    // nothing to do here
    ck_assert(true);
  }
}

Suite *make_signal_suite() {
  Suite *s = suite_create("signal");
  TCase *tc = tcase_create("core");
  suite_add_tcase(s, tc);

  tcase_add_test(tc, signal_waitpid_ignore_child_test);
  tcase_add_test(tc, signal_spawn_child_test);

  return s;
}
