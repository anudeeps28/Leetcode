#include<iostream>
#include<unordered_map>
using namespace std;

class Solution {
public:
    bool isAnagram(string s, string t) {
        unordered_map<char, int> m;
        for (auto i: s) {
            m[i]++;
        }
        for (auto i: t) {
            m[i]--;
        }

        for (auto [key, value]: m) {
            if (value != 0) {
                return false;
            }
        }
        return true;
    }
};