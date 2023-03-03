#include<iostream>
#include<string>
#include<vector>
#include<stack>

using namespace std;
class Solution {

public:
    int evalRPN(vector<string>& tokens) {
        stack<int> numbers;
        for(int i = 0; i < tokens.size(); i++) {
            if (isdigit(stoi(tokens[i]))) {
                numbers.push(stoi(tokens[i]));
            }
        }
    }
};

int main () {
    Solution s;
    vector<string> expression = {"2", "1", "+", "3", "*"};
    cout << s.evalRPN(expression) << endl;
    
}