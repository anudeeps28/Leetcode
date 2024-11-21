#include<iostream>
#include<vector>
#include<unordered_set>
using namespace std;

class Solution {
public:
    // solution 1
    bool containsDuplicate(vector<int>& nums) {
        unordered_set<int> s;
        
        for (int i = 0; i < nums.size(); i++) {
            if (s.find(nums[i]) != s.end()) {
                return true;
            }
            s.insert(nums[i]);
        }
        
        return false;
    }

    // solution 2
    bool containsDuplicate(vector<int>& nums) {
        unordered_map<int, int> m;

        for (auto i: nums) {
            m[i]++;
        }

        bool duplicate = false;

        for (auto [key, value]: m) {
            if (value > 1) {
                duplicate = true;
            }
        }
        return duplicate;
    }
};



    



int main() {
    Solution s;
    vector<int> v = {1,2,3};
    cout << s.containsDuplicate(v) << endl;

}