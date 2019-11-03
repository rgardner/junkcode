#include <algorithm>
#include <future>
#include <iostream>
#include <numeric>
#include <vector>

#include <catch2/catch.hpp>

template <typename RAIter>
int parallel_sum(RAIter begin, RAIter end) {
  auto len = end - begin;
  if (len < 1000) return std::accumulate(begin, end, 0);

  RAIter mid = begin + len / 2;
  auto handle = std::async(std::launch::async, parallel_sum<RAIter>, mid, end);
  int sum = parallel_sum(begin, mid);
  return sum + handle.get();
}

TEST_CASE("async_parallel_sum_test", "[async]") {
  std::vector<int> v(10000, 1);
  const auto result = parallel_sum(v.begin(), v.end());
  CHECK(result == 10000);
}
