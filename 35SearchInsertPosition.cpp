#include<iostream>
#include<vector>
#include<algorithm>
using namespace std;

class Solution {
public:
    int searchInsert(vector<int>& nums, int target) {
        int length = nums.size();

        auto it = find(nums.begin(), nums.end(), target);
        if (it == nums.end()) {
            int j = 0;
            while(target > nums[j]) {
                j++;
            }
            return j;
        } else {
            return it - nums.begin();
        }

       
    }
};

int main() {
Solution s;
vector<int> vec = {1,3,7,9,11};
int toFind = 8;

int answer = s.searchInsert(vec, toFind);
cout << answer << endl;

}