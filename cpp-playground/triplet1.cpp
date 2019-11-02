#include <algorithm>
#include <map>
#include <iostream>
#include <set>
#include <tuple>
#include <vector>

class Solution {
public:
    std::vector<std::vector<int>> threeSum(const std::vector<int>& nums) {
        const auto sums = makeSumsTable(nums);
        std::vector<std::vector<int>> result;
        for (int i = 0; i < nums.size(); ++i) {
            const int complement = -nums[i];
            const auto found = sums.find(complement);
            if (found != sums.end()) {
                const auto [bIndex, cIndex] = found->second;
                if ((i == bIndex) || (i == cIndex)) {
                    continue;
                }

                std::vector<int> triplet{ nums[i], nums[bIndex], nums[cIndex] };
                std::sort(triplet.begin(), triplet.end());

                const auto found = std::any_of(std::begin(result), std::end(result), triplet);
                if (!found) {
                    result.emplace_back(std::move(triplet));
                }
            }
        }

        return result;
    }

    // sum -> (i, j)
    std::map<int, std::tuple<int, int>> makeSumsTable(const std::vector<int>& nums) {
        std::map<int, std::tuple<int, int>> sums;
        for (int i = 0; i < nums.size() - 1; ++i) {
            for (int j = i + 1; j < nums.size(); ++j) {
                sums[nums[i] + nums[j]] = std::make_tuple(i, j);
            }
        }

        return sums;
    }
};

int main() {
    Solution s;
    const auto solution = s.threeSum({ -1, 0, 1, 2, -1, -4});
    for (const auto& res : solution) {
        std::cout << "a: " << res[0] << ", "
                  << "b: " << res[1] << ", "
                  << "c: " << res[2] << "\n";
    }
}
