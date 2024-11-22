#include <iostream>
#include <unordered_set>
#include <vector>
using namespace std;

bool hasPairWithSum(vector<int>& nums, int target) {
    unordered_set<int> seenNumbers; // To store numbers we've seen so far

    for (int num : nums) {
        int complement = target - num;

        // Check if the complement exists in the set
        if (seenNumbers.find(complement) != seenNumbers.end()) {
            return true; // Pair found
        }

        // Add the current number to the set
        seenNumbers.insert(num);
    }

    return false; // No pair found
}

int main() {
    vector<int> nums = {1, 2, 4, 4};
    int target = 8;

    if (hasPairWithSum(nums, target)) {
        cout << "True" << endl; // Pair exists
    } else {
        cout << "False" << endl; // No pair exists
    }

    return 0;
}
