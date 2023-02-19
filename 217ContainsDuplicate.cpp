#include<iostream>
#include<vector>
using namespace std;

class Solution {
public:
    bool containsDuplicate(vector<int>& nums) {
        sort(nums.begin(), nums.end());
        for (int i = 0; i < nums.size(); i++) {
            if (nums[i] == nums[i+1]){
                return true;
            }
        }
        return false;
    }
};

int main() {
    Solution s;
    vector<int> v = {1,2,3};
    cout << s.containsDuplicate(v) << endl;

}