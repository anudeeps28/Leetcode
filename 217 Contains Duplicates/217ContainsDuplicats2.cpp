#include <iostream>
#include <unordered_set>
#include <vector>

class Solution {
public:
    bool containsDuplicate(std::vector<int>& nums) {
        std::unordered_set<int> seen;

        for (int i : nums) {
            if (seen.count(i)) {
                return true; // Duplicate found
            }
            seen.insert(i);
        }
        return false; // No duplicates
    }
};
