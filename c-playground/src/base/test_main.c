#include <stdlib.h>

#include <check.h>

#include "test_suites.h"

int main() {
  SRunner* sr = srunner_create(make_endian_suite());
  srunner_add_suite(sr, make_move_last_suite());
  srunner_add_suite(sr, make_signal_suite());

  srunner_run_all(sr, CK_VERBOSE);
  const int num_failed = srunner_ntests_failed(sr);
  srunner_free(sr);
  return (num_failed == 0) ? EXIT_SUCCESS : EXIT_FAILURE;
}
