#include <cassert>
#include <map>
#include <string>

enum class ParenType {
    None = 0,
    Paren,
    CurlyBrace,
    Bracket,
};

bool has_balanced_parens(const std::string& string);
ParenType update_paren_map(std::map<ParenType, int>& paren_map, const char c);

int main()
{
    const char* s1 = "()";
    const char* s2 = ")";
    const char* s3 = "))";
    const char* s4 = "(()";
    const char* s5 = "(()()(((())()()())()))))";
    const char* s6 = "(((((()()))()())()))(()())";

    assert(has_balanced_parens(s1));
    assert(!has_balanced_parens(s2));
    assert(!has_balanced_parens(s3));
    assert(!has_balanced_parens(s4));
    assert(!has_balanced_parens(s5));
    assert(has_balanced_parens(s6));
}


bool has_balanced_parens(const std::string& string)
{
    if ((string.size() & 1) != 0)
    {
        return false;
    }

    std::map<ParenType, int> paren_map = {
        {ParenType::Paren, 0},
        {ParenType::CurlyBrace, 0},
        {ParenType::Bracket, 0},
    };

    for (const auto& c : string)
    {
        const ParenType paren = update_paren_map(paren_map, c);
        if ((paren != ParenType::None) && paren_map[paren] < 0)
        {
            return false;
        }
    }

    return true;
}

ParenType update_paren_map(std::map<ParenType, int>& paren_map, const char c)
{
    switch (c)
    {
    case '(':
        ++paren_map[ParenType::Paren];
        return ParenType::Paren;

    case ')':
        --paren_map[ParenType::Paren];
        return ParenType::Paren;

    case '{':
        ++paren_map[ParenType::CurlyBrace];
        return ParenType::CurlyBrace;

    case '}':
        --paren_map[ParenType::CurlyBrace];
        return ParenType::CurlyBrace;

    case '[':
        ++paren_map[ParenType::Bracket];
        return ParenType::Bracket;

    case ']':
        --paren_map[ParenType::Bracket];
        return ParenType::Bracket;

    default:
        return ParenType::None;
    }
}
