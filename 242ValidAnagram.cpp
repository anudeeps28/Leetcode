#include<iostream>
#include<string>
#include<unordered_set>
using namespace std;

class Solution {
public:
    bool isAnagram(string s, string t) {
        unordered_set<char> s1;
        unordered_set<char> s2;

        for (int i = 0; i < s.size(); i ++) {
            s1.insert(s[i]);
        }
        for (int i = 0; i < t.size(); i ++) {
            s2.insert(t[i]);
        }

        if (s1 == s2) {
            return true;
        }
        return false;
    }
};

int main () {
    Solution S;
    string s = "anagram";
    string t = "nagaram";

    cout << S.isAnagram(s, t) << endl;
}