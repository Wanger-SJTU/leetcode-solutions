#include "leetcode.h"
/**
 * Definition for a binary tree node.
 * struct TreeNode {
 *     int val;
 *     TreeNode *left;
 *     TreeNode *right;
 *     TreeNode(int x) : val(x), left(NULL), right(NULL) {}
 * };
 */
class Solution {
private:
    vector<int> res;
public:
    vector<int> inorderTraversal(TreeNode* root) {
        Helper(root);
        return res;
    }
    void Helper(TreeNode* root) {
        if (root == nullptr) {
            return;
        }
        
        if (root->left != nullptr) {
            Helper(root->left);
           // res.push_back(root->left->val);
        }
        res.push_back(root->val);
        if (root->right != nullptr) {
            Helper(root->right);
            //res.push_back(root->right->val);
        }
    }
};