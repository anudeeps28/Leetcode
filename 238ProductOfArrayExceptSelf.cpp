#include<iostream>
#include<vector>
using namespace std;

class Solution {
public:
    vector<int> productExceptSelf(vector<int>& nums) {
        vector<int> answer;
        for (int i = 0; i < nums.size(); i++) {
            int temp = 1;
            for (int j = 0; j < nums.size(); j++) {
                if (i != j) {
                    temp = temp*nums[j];
                }
            }
            answer.push_back(temp);
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