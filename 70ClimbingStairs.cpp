#include<iostream>
class Solution {
public:
    int climbStairs(int n) {
        if (n < 0) return 0;
        if (n == 1 || n == 0) return 1;
        
        return climbStairs(n-1) + climbStairs(n-2);
    }
};

using namespace std;

int main() {
    Solution s;
    int n = 4;
    cout << s.climbStairs(n) << endl;
}