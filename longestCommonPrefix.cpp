#include<iostream>
#include<vector>
#include<string>
#include<set>
#include<algorithm>

using namespace std;

class Solution {
public:
    string longestCommonPrefix(vector<string>& strs) {
        string answer = "";
        int n = strs.size();
        
        sort(strs.begin(), strs.end());
        
        string A = strs[0];
        string B = strs[n-1];

        for (int i = 0; i < A.size(); i++) {
            if (A[i] == B[i]) {
                answer += A[i];
            } else {
                break;
            }
        }
        return answer;
    }
    
};

int main() {
    Solution s;
    vector<string> v = {"flower","flow","flight"};

    cout << s.longestCommonPrefix(v) << endl;


   
}