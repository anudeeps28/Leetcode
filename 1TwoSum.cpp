#include<iostream>
#include<vector>
using namespace std;

class Solution {
public:
    vector<int> twoSum(vector<int>& nums, int target) {
        vector <int> ret;
        int size = nums.size();

        for (int i = 0; i < size; i++)
        {
            for (int j = i+1; j < size; j++)
            {
                if(nums[i] + nums[j] == target)
                {
                    ret.push_back(i);
                    ret.push_back(j);
                    return ret;
                }
            }
        }
        return ret;
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