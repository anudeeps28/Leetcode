#include<iostream>
#include<vector>
using namespace std;

class Solution {
public:
    int climbStairs(int n) {
        vector<int> dp(n+1);
        dp[0]=dp[1]=1;
        for(int i=2;i<=n;i++)   
            dp[i]=dp[i-1]+dp[i-2];
        return dp[n];
    }
};

using namespace std;

int main() {
    Solution s;
    int n = 4;
    cout << s.climbStairs(n) << endl;
}