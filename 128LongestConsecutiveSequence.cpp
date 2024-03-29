#include<iostream>
#include<vector>
#include<unordered_set>
using namespace std;

class Solution {
public:
    int longestConsecutive(vector<int>& nums) {
        unordered_set<int>s(nums.begin(), nums.end());
        int longest = 0;
        for(auto &n: s){
            //if this is the start of the sequence
            if(!s.count(n - 1)){
                int length = 1; 
                while(s.count(n + length))
                    ++length;
                longest = max(longest, length);
            } 

        }
        return longest;
    }
};

int main () {
    Solution s;
    vector<int> numbers = {100,4,200,1,3,2};
    cout << s.longestConsecutive(numbers) << endl;

}