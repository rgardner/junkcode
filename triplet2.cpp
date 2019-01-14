using namespace std;
#include <vector>

#include <map>

class Solution {
public:
    vector<vector<int>> threeSum(vector<int>& nums) {
        const auto sums = makeSumsTable(nums);

        std::vector<std::vector<int>> result;
        for (int i = 0; i < nums.size(); ++i) {
            const int complement = -nums.at(i);
            const auto found = sums.find(complement);
            if (found != sums.end()) {
                const int bIndex = found->second.at(0);
                const int cIndex = found->second.at(1);
                if ((i == bIndex) || (i == cIndex)) {
                    continue;
                }
                
                const auto triplet = makeSortedTriplet(nums[i], nums[bIndex], nums[cIndex]);
                bool found = false;
                for (const auto& res : result) {
                    if (res == triplet) {
                        found = true;
                        break;
                    }
                }
                
                if (!found) {
                    result.emplace_back(std::move(triplet));
                }
            }
        }
        
        return result;
    }
    
    // sum -> (i, j)
    static std::map<int, std::vector<int>> makeSumsTable(const vector<int>& nums) {
        std::map<int, std::vector<int>> sums;
        for (int i = 0; i < nums.size() - 1; ++i) {
            for (int j = i + 1; j < nums.size(); ++j) {
                sums[nums.at(i) + nums.at(j)] = { i , j };
            }
        }
        
        return sums;
    }
    
    static std::vector<int> makeSortedTriplet(int a, int b, int c) {
        int minAB = (a < b) ? a : b;
        int maxAB = (a > b) ? a : b;
        if (c < minAB) {
            return { c, minAB, maxAB };
        } else if (c > maxAB) {
            return { minAB, maxAB, c };
        } else {
            return { minAB, c, maxAB };
        }
    }
};
