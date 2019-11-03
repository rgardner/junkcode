#include <array>
#include <cassert>
#include <functional>
#include <string_view>

#include <catch2/catch.hpp>

enum ParenType {
  ParenTypeParen = 0,
  ParenTypeCurlyBrace,
  ParenTypeBracket,
};

// Checks if a string has matching parentheses.
//
// Examples:
// has_balanced_parens2("{()[]}") == true
// has_balanced_parens2(")") == false
// has_balanced_parens2("())") == false
// has_balanced_parens2("{())") == false
bool has_balanced_parens2(std::string_view str) {
  std::array paren_type_counts{0, 0, 0};
  for (auto c : str) {
    if (c == '(') {
      ++paren_type_counts[ParenTypeParen];
    } else if (c == ')') {
      if (paren_type_counts[ParenTypeParen] <= 0) return false;
      --paren_type_counts[ParenTypeParen];
    } else if (c == '{') {
      ++paren_type_counts[ParenTypeCurlyBrace];
    } else if (c == '}') {
      if (paren_type_counts[ParenTypeCurlyBrace] <= 0) return false;
      --paren_type_counts[ParenTypeCurlyBrace];
    } else if (c == '[') {
      ++paren_type_counts[ParenTypeBracket];
    } else if (c == ']') {
      if (paren_type_counts[ParenTypeBracket] <= 0) return false;
      --paren_type_counts[ParenTypeBracket];
    }
  }

  return std::all_of(paren_type_counts.cbegin(), paren_type_counts.cend(),
                     [](int count) { return count == 0; });
}

TEST_CASE("validate_parens_just_parens_test", "[validate_parens]") {
  CHECK(has_balanced_parens2("()"));
  CHECK(!has_balanced_parens2(")"));
  CHECK(!has_balanced_parens2("(()"));
  CHECK(has_balanced_parens2(""));
}

TEST_CASE("validate_parens_mixed_parens_test", "[validate_parens]") {
  CHECK(has_balanced_parens2("{()}[]"));
  CHECK(!has_balanced_parens2("{()"));
  CHECK(!has_balanced_parens2("){}"));
  CHECK(!has_balanced_parens2("(()]"));
}
