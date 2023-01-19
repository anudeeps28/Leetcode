#include<iostream>
#include<vector>
using namespace std;

// class Solution {
// public:
//     vector<int> plusOne(vector<int>& digits) {
//         int lastElement = *(digits.end()-1);
//         if (lastElement != 9) {
//             lastElement += 1;
//         } else {
//             for (int i = digits.size()-1; i > -1; i--) {
//                 while (digits[i] != 9) {
//                     digits[i] = 0;
//                     digits[i-1] += 1;
//                     cout << digits[i] << " " << digits[i-1] << endl;
//                 }
//             }
//         }
//         // cout << lastElement;

//         return digits;
//     }
// };

class Solution {
public:
    vector<int> plusOne(vector<int>& digits) {
      int n = digits.size() - 1;
      
      for (int i = n; i >= 0; --i) { 
        if (digits[i] == 9) {  
            digits[i] = 0;
        } else {  
            digits[i] += 1;
            return digits;
        }
      }
      
      digits.push_back(0);
      digits[0] = 1;

      
      return digits;

    }
};

int main() {
    Solution S;

    vector<int> array = {1,2,3};

    S.plusOne(array);

   
}