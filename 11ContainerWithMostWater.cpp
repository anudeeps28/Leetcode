#include<iostream>
#include<vector>
using namespace std;

class Solution {
public:
    int maxArea(vector<int>& height) {
        int i = 0; 
        int j = height.size() - 1;

        int current = 0;
        int result = 0;

        while (i < j) {
            current = (j-i)*min(height[i], height[j]);
            result = max(current, result);

            if (height[i] <= height[j]) {
                i++;
            } else {
                j--;
            }
        }
        return result;

    }
};

int main() {
    Solution s;
    vector<int>numbers = {1,8,6,2,5,4,8,3,7};
    int area = s.maxArea(numbers);

    cout << area;
}