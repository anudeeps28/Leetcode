#include<iostream>
#include<string>
#include<vector>
using namespace std;

class Solution {
public:
    bool isAnagram(string s, string t) {
        if (s.size() != t.size()) {
            return false;
        }
        int array[26] = {0};
        for (int i = 0; i < s.size(); i++) {
            array[s[i] - 'a']++;
            array[t[i] - 'a']--;
        }
        for (int i = 0; i < 26; i++)
            if (array[i]) return false;
        return true;
        
    }
};

int main () {
    Solution S;
    string s = "anagram";
    string t = "nagaram";

    cout << S.isAnagram(s, t) << endl;
}