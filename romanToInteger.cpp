#include<iostream>
#include<unordered_map>
#include<string>
using namespace std;

class Solution {
public:
    int romanToInt(string s) {
        unordered_map<char, int> m;
        m['I'] = 1;
        m['V'] = 5;
        m['X'] = 10;
        m['L'] = 50;
        m['C'] = 100;
        m['D'] = 500;
        m['M'] = 1000;

        int integer = 0;
        for (int i = 0; i < s.size(); i++) {
            if (m[s[i]] < m[s[i+1]]) {
                integer -= m[s[i]];
            } else {
                integer += m[s[i]];
            }
        }
        return integer;
    }   
};

int main() {
    string str = "III";
    Solution s;
    int answer;

    answer = s.romanToInt(str);
    cout << answer;
}