#include<iostream>
#include<string>
#include<vector>
#include<algorithm>
using namespace std;

class Solution {
public:
    bool isAnagram(string s, string t) {

        sort(s.begin(), s.end());
        sort(t.begin(), t.end());

        if (s == t) {
            return true;
        } else {
            return false;
        }
        
    }
};

int main () {
    Solution S;
    string s = "anagram";
    string t = "nagaram";

    cout << S.isAnagram(s, t) << endl;
}