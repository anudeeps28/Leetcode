#include<iostream>
#include<vector>
#include<map>
using namespace std;

class Solution {
public:
    vector<int> topKFrequent(vector<int>& nums, int k) {
        vector<int> answer;
        map<int, int> mp;

        for (int i = 0; i < nums.size(); i++) {
            mp[nums[i]]++;
        }

        auto it = mp.begin();
        answer.push_back((*it).first);

        it++;

        answer.push_back((*it).first);
        
        return answer;
    }
};

int main () {
    Solution s;
    vector<int> numbers = {1,1,1,2,2,3};
    int k = 2;
    vector<int> finalAnswer = s.topKFrequent(numbers,k);

    for (auto i: finalAnswer) {
        cout << i << " ";
    }
}