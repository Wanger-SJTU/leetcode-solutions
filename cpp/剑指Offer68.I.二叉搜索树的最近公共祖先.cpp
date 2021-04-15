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
public:
    TreeNode* lowestCommonAncestor(TreeNode* root, TreeNode* p, TreeNode* q) {
        TreeNode* left = p->val > q->val ? q : p; 
        TreeNode* right = p->val > q->val ? p : q;
        if (root->val > left->val && root->val < right->val) {
            return root;
        } else if (root->val > right->val) {
            return lowestCommonAncestor(root->left, p, q);
        } else if (root->val < left->val){
            return lowestCommonAncestor(root->right, p, q);
        }
        return root;
    }
};