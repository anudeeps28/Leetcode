#include<iostream>
#include<stack>
using namespace std;

class MinStack {
public:
    MinStack() {
        
    }
    
    void push(int val) {
        stk.push(val);
        if (minStk.empty()) {
            minStk.push(val);
        } else if (val < minStk.top()) {
            minStk.push(val);
        } else if(val > minStk.top()) {
            minStk.push(minStk.top());
        }

    }
    
    void pop() {
        stk.pop();
        minStk.pop();
        
    }
    
    int top() {
        return stk.top();
        
    }
    
    int getMin() {
        return minStk.top();
        
    }
private:
    stack<int> stk;
    stack<int> minStk;

};

int main () {
    MinStack s;

}