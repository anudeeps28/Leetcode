#include<iostream>
#include<vector>
#include<numeric>
using namespace std;

class Solution {
public:
    vector<int> productExceptSelf(vector<int>& nums) {
        vector<int> answer;
        for (int i = 0; i < nums.size(); i++) {
            int temp;
            int product;
            temp = nums[i];
            nums[i] = 1;
            product = accumulate(nums.begin(), nums.end(), 1, multiplies<int>());
            answer.push_back(product);
            nums[i] = temp;
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