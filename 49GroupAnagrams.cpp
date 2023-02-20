#include<iostream>
#include<vector>
#include<string>
#include<unordered_map>
using namespace std;

class Solution {
public:
    vector<vector<string>> groupAnagrams(vector<string>& strs) {
        unordered_map<string, vector<string>> mp; 
        for (auto s: strs) {
            string t = s;
            sort(t.begin(), t.end());
            mp[t].push_back(s);
        }

        vector<vector<string>> answer;
        for (auto i: mp) {
            answer.push_back(i.second);
        }
        return answer;
        
    }
};

int main () {
    Solution s;
    vector<string> v = {"eat","tea","tan","ate","nat","bat"};
    vector<vector<string>> answer = s.groupAnagrams(v);

    for (int i = 0; i < answer.size(); i++) {
        for (int j = 0; j < answer[i].size(); j++) {
            cout << answer[i][j] << " ";
        }
        cout << endl;
    }
}