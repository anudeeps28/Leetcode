
#include<iostream>
using namespace std;

struct TreeNode
{
    int val;
    TreeNode *left;
    TreeNode *right;
    TreeNode() : val(0), left(nullptr), right(nullptr) {}
    TreeNode(int x) : val(x), left(nullptr), right(nullptr) {}
    TreeNode(int x, TreeNode *left, TreeNode *right) : val(x), left(left), right(right) {}
};

class Solution
{
private:
    bool isSymmetricHelper(TreeNode* leftSubTree, TreeNode* rightSubTree) {
        if (leftSubTree == nullptr && rightSubTree == nullptr) {
            return true;
        } else if (leftSubTree == nullptr || rightSubTree == nullptr) {
            return false;
        } else if (leftSubTree->val != rightSubTree->val) {
            return false;
        }
        return isSymmetricHelper(leftSubTree->left, rightSubTree->right) && isSymmetricHelper(leftSubTree->right, rightSubTree->left);
    }

public:
    bool isSymmetric(TreeNode *root) {
        if (root == nullptr) {
            return true;
        }   
        return isSymmetricHelper(root->left, root->right);
    }
};

int main () {
    Solution s;
    TreeNode* node1 = new TreeNode(3);
    TreeNode* node2 = new TreeNode(4);
    TreeNode* node3 = new TreeNode(4);
    TreeNode* node4 = new TreeNode(3);

    TreeNode* node5 = new TreeNode(2, node1, node2);
    TreeNode* node6 = new TreeNode(2, node3, node4);
    
    TreeNode* node7 = new TreeNode(1, node5, node6);


}