#include<iostream>
#include<vector>
#include<unordered_map>
using namespace std;

vector<int> moreThanOnce(vector<int> v) {
    unordered_map<int, int> m;
    for (auto i: v) {
        m[i]++;
    }

    vector<int> answer;
    for (auto [key,value]: m) {
        if (value > 1) {
            answer.push_back(key);
        }
    }

    return answer;
}


int main() {
    vector<int> v;
    v.push_back(4);
    v.push_back(5);
    v.push_back(6);
    v.push_back(4);
    v.push_back(7);
    v.push_back(5);
    
    vector<int> final = moreThanOnce(v);
    for (auto i: final) {
        cout << i << endl;
    }
    return 0;
}