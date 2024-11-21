#include<iostream>
#include<vector>
#include<unordered_map>
using namespace std;

void FrequencyOfElements(vector<int> v){
    unordered_map<int, int> m;
    for (auto i: v) {
        m[i]++;     
    }

    for (auto [key, value]: m) {
        cout << key << "->" << value << endl;
    }
}

int main() {
    vector<int> v;
    v.push_back(1);
    v.push_back(2);
    v.push_back(2);
    v.push_back(4);
    v.push_back(1);
    
    FrequencyOfElements(v);
    return 0;
}