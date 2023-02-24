#include<iostream>
#include<string>
#include<vector>
#include<unordered_map>
#include<algorithm>
using namespace std;

class Solution {
public:
    bool isAnagram(string s, string t) {
        unordered_map <char, int> smap;
        unordered_map <char, int> tmap;

        if (s.size() != t.size()) {
            return false;
        }
        for (int i = 0; i < s.size(); i++) {
            smap[s[i]]++;
            tmap[t[i]]++;
        }

        for (int i = 0; i < s.size(); i++) {
            if (smap[i] != tmap[i]) {
                return false;
            } 
        }
        return true;
        
    }
};

int main () {
    Solution S;
    string s = "anagram";
    string t = "nagaram";

    cout << S.isAnagram(s, t) << endl;
}