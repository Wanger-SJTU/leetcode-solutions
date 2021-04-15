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
    TreeNode* mergeTrees(TreeNode* t1, TreeNode* t2) {
        if(nullptr == t1) return t2;
        if(nullptr == t2) return t1;
        t1->val += t2->val;
        // if(t2->left && nullptr == t1->left){
        //     t1->left = t2->left;
        //     return t1;
        // }
        // if(t2->right && nullptr == t1->right){
        //     t1->right = t2->right;
        //     return t1;
        // }
        
        t1->left = mergeTrees(t1->left,t2->left);
        t1->right = mergeTrees(t1->right,t2->right);
        return t1;
    }

};