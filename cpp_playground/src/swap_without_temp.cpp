#include <catch2/catch.hpp>

void add_swap(int* a, int* b) {
  *a = *a + *b;
  *b = *a - *b;
  *a = *a - *b;
}

void bit_swap(int* a, int* b) {
  *a = *a ^ *b;
  *b = *a ^ *b;
  *a = *a ^ *b;
}

void multiply_divide_swap(int* a, int* b) {
  *a = *a * *b;
  *b = *a / *b;
  *a = *a / *b;
}

TEST_CASE("add_swap works", "[algorithm]") {
  int a = -1;
  int b = 8;
  add_swap(&a, &b);
  CHECK(a == 8);
  CHECK(b == -1);
}

TEST_CASE("bit_swap works", "[algorithm]") {
  int a = -1;
  int b = 8;
  bit_swap(&a, &b);
  CHECK(a == 8);
  CHECK(b == -1);
}

TEST_CASE("multiply_divide_swap works", "[algorithm]") {
  int a = -1;
  int b = 8;
  multiply_divide_swap(&a, &b);
  CHECK(a == 8);
  CHECK(b == -1);
}