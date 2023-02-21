#include<iostream>
#include<vector>
using namespace std;

class Solution {
public:
    int longestConsecutive(vector<int>& nums) {
        if (nums.empty()) {
            return 0;
        }
        sort(nums.begin(), nums.end());

        int counter = 0;
        for (int i = 0; i < nums.size(); i++) {
            if (nums[i] + 1 == nums[i+1]) {
                counter++;
            }
        }
        return counter+1;
    }
};

int main () {
    Solution s;
    vector<int> numbers = {100,4,200,1,3,2};
    cout << s.longestConsecutive(numbers) << endl;

}