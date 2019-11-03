#include <assert.h>
#include <stdlib.h>

#include "test_suites.h"

#define ARRAYSIZE(a) (sizeof(a) / sizeof(a[0]))

void swap(int* a, int* b) {
  const int temp = *a;
  *a = *b;
  *b = temp;
}

void move_last(int* values, int num_values, int idx) {
  assert(idx < num_values);

  for (int i = idx; i < (num_values - 1); i++) {
    swap(&values[i], &values[i + 1]);
  }
}

START_TEST(move_last_test) {
  int values[] = {2, 3, 5, 7, 11, 13, 17, 19};
  move_last(values, ARRAYSIZE(values), 2);

  ck_assert_int_eq(values[0], 2);
  ck_assert_int_eq(values[1], 3);
  ck_assert_int_eq(values[2], 7);
  ck_assert_int_eq(values[3], 11);
  ck_assert_int_eq(values[4], 13);
  ck_assert_int_eq(values[5], 17);
  ck_assert_int_eq(values[6], 19);
  ck_assert_int_eq(values[7], 5);
}
END_TEST

Suite* make_move_last_suite() {
  Suite* s = suite_create("move_last");
  TCase* tc = tcase_create("core");
  suite_add_tcase(s, tc);

  tcase_add_test(tc, move_last_test);

  return s;
}
