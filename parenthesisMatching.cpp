#include<iostream>
#include<stack>
#include<string>

using namespace std;

class Solution {
public:
    bool isValid(string s) {
        stack<char> stk;
        for (int i = 0; i < s.length(); i++) {
            if (s[i] == '(' || s[i] == '{' || s[i] == '[') {
                stk.push(s[i]);
                continue;
            }
            
            if (stk.empty()) {
                return false;
            }

            if ((stk.top() == '(' && s[i] != ')') || (stk.top() == '{' && s[i] != '}') || (stk.top() == '[' && s[i] != ']')) {
                return false;
            }
            stk.pop();
        }
        return stk.empty();
    }
};

int main() {
    string s = "(){}}{";

    Solution S;
    cout << S.isValid(s);
}