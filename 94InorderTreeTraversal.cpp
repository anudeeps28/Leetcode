#include <iostream>
#include <vector>
#include <stack>
using namespace std;

struct TreeNode {
    int val;
    TreeNode *left;
    TreeNode *right;
    TreeNode() : val(0), left(nullptr), right(nullptr) {}
    TreeNode(int x) : val(x), left(nullptr), right(nullptr) {}
    TreeNode(int x, TreeNode *left, TreeNode *right) : val(x), left(left), right(right) {}
};

class Solution {
public:
    vector<int> inorderTraversal(TreeNode* root) {
        vector<int> nodes;
        stack<TreeNode*> todo;
        while (root || !todo.empty()) {
            while (root) {
                todo.push(root);
                root = root -> left;
            }
            root = todo.top();
            todo.pop();
            nodes.push_back(root -> val);
            root = root -> right;
        }
        return nodes;
    }
};

int main() {
    Solution sol;
    TreeNode node3(3);
    TreeNode node2(2, nullptr, &node3);
    TreeNode node1(1, &node2, nullptr);

    TreeNode* root = &node1;
    vector<int> inorder = sol.inorderTraversal(root);
    for (auto i : inorder) {
        cout << i << endl;
    }
    return 0;
}
