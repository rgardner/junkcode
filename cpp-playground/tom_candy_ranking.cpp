#include <algorithm>
#include <cassert>
#include <iostream>
#include <iterator>
#include <map>
#include <numeric>
#include <vector>

const int c_min_candies = 1;

std::vector<int> distribute_candies1(const std::vector<int>& rankings);
std::vector<int> distribute_candies2(const std::vector<int>& rankings);
void display_rankings_and_candies(const std::vector<int>& rankings, const std::vector<int>& candies);

int main(int argc, char** argv)
{
    // input: rankings for each people
    // output: number of candies to give to each person s.t. if ranking(a) > ranking(b), then candy(a) > candy(b)
    // minimize total number of candies given out
    const std::vector<int> rankings1{1,2,3,4};
    const std::vector<int> candies1 = distribute_candies1(rankings1);
    display_rankings_and_candies(rankings1, candies1);
    assert(std::accumulate(candies1.begin(), candies1.end(), 0 /*initial value*/) == 10);

    const std::vector<int> rankings2{38, 1, 4, 3};
    const std::vector<int> candies2 = distribute_candies2(rankings2);
    display_rankings_and_candies(rankings2, candies2);
    assert(std::accumulate(candies2.begin(), candies2.end(), 0 /*initial value*/) == 10);

    return EXIT_SUCCESS;
}

// strategies

// 1) give candies equal to ranking
//    pros: simple, one pass
//    cons: gives away too much candy!
std::vector<int> distribute_candies1(const std::vector<int>& rankings)
{
    std::vector<int> candies(rankings.size());
    std::transform(rankings.begin(), rankings.end(), candies.begin(), [](int ranking) { return ranking; } );
    return candies;
}

// 2) sort and for_each with state: (prev_ranking, prev_candy)
//    pros: gives away right amount of candy
//    cons: slightly more complex to implement, requires two passes
// precondition: rankings is non-empty
std::vector<int> distribute_candies2(const std::vector<int>& rankings)
{
    assert(!rankings.empty());

    // key: ranking, value: index in rankings
    // map sorts the keys
    std::map<int, std::size_t> sorted_rankings;
    for (std::size_t i = 0; i < rankings.size(); ++i) {
        sorted_rankings[rankings[i]] = i;
    }

    std::vector<int> candies(sorted_rankings.size());
    auto it = sorted_rankings.begin();
    candies[it->second] = c_min_candies;
    ++it;
    for ( ; it != sorted_rankings.end(); ++it)
    {
        const int ranking = it->first;
        const int rankings_idx = it->second;
        const auto prev_elem = std::prev(it);

        if (ranking == prev_elem->first) {
            candies[rankings_idx] = candies[prev_elem->second];
        } else if (ranking > prev_elem->first) {
            candies[rankings_idx] = candies[prev_elem->second] + 1;
        } else {
            assert(false);
        }
    }

    return candies;
}

// utils

void display_rankings_and_candies(const std::vector<int>& rankings, const std::vector<int>& candies)
{
    for (int i = 0; i < rankings.size(); ++i)
    {
        std::cout << "ranking: " << rankings[i] << "\tcandies: "<< candies[i] << std::endl;
    }
}
