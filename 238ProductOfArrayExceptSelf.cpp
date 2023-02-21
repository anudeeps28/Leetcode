#include<iostream>
#include<vector>
#include<numeric>
using namespace std;

class Solution {
public:
    vector<int> productExceptSelf(vector<int>& nums) {
        vector<int> answer(nums.size(), 1);
        
        int temp = 1;
        for (int i = 0; i < nums.size(); i++) {
            answer[i] = temp;
            temp = temp*nums[i];
        }

        int temp2 = 1;
        for (int i = nums.size()-1; i >= 0; i--) {
            answer[i] = answer[i]*temp2;
            temp2 = temp2* nums[i];
        }

        return answer;

    }
};


int main() {
    Solution s;
    vector<int> numbers = {1,2,3,4};
    vector<int> finalAnswer = s.productExceptSelf(numbers);

    for (auto i: finalAnswer) {
        cout << i << endl;
    }


}