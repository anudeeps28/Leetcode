#include<iostream>
#include<vector>
#include<unordered_map>
using namespace std;

class Solution {
public:
    vector<int> twoSum(vector<int>& nums, int target) {
        unordered_map<int, int> m;
        vector<int> result;
        for (int i = 0; i < nums.size(); i++) {
            int complement = target - nums[i];
            if (m.find(complement) != m.end()) {
                result.push_back(i);
                result.push_back(m[complement]);
            } else {
                m.insert({nums[i], i});
            }
        }
        return result;
    }
};

int main () {
    Solution s;
    
    vector<int> numbers = {3,2,4};

    int target = 6;
    vector<int> answer = s.twoSum(numbers, target);

    for (auto i: answer) {
        cout << i << endl;
    }

}