#include<iostream>
#include<vector>
using namespace std;

class Solution {
public:
    int helperFunction(vector<int> &dp, int n) {
        if (n < 0) return 0;
        if (n == 1 || n == 0) return 1;

        if (dp[n] != -1) {
            return dp[n];
        }

        return dp[n] = helperFunction(dp, n-1) + helperFunction(dp, n-2);
    }

    int climbStairs(int n) {
        
        vector<int> dp(n+1, -1); // initializing (n+1) elements with -1
        return helperFunction(dp, n);

    }
};

using namespace std;

int main() {
    Solution s;
    int n = 4;
    cout << s.climbStairs(n) << endl;
}