#include <stdint.h>

#include "test_suites.h"

enum endian {
  c_endian_unknown = 0,
  c_endian_little = 1,
  c_endian_big = 2,
};

// From Stanford's Intro to Computer Networking
enum endian get_endian() {
  uint16_t val = 0x400;
  uint8_t *ptr = (uint8_t *)&val;

  if (ptr[0] == 0x40) {
    return c_endian_big;
  } else if (ptr[1] == 0x40) {
    return c_endian_little;
  } else {
    return c_endian_unknown;
  }
}

START_TEST(endian_test) { ck_assert_int_eq(get_endian(), c_endian_unknown); }
END_TEST

Suite *make_endian_suite() {
  Suite *s = suite_create("endian");
  TCase *tc = tcase_create("core");
  suite_add_tcase(s, tc);

  tcase_add_test(tc, endian_test);

  return s;
}
