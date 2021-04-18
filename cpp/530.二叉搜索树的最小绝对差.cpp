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
public:
    void dfs(TreeNode* root, int& pre, int& ans) {
        if (root == nullptr) {
            return;
        }
        dfs(root->left, pre, ans);
        if (pre == -1) {
            pre = root->val;
        } else {
            ans = min(ans, root->val - pre);
            pre = root->val;
        }
        dfs(root->right, pre, ans);
    }
    int getMinimumDifference(TreeNode* root) {
        int ans = INT_MAX, pre = -1;
        dfs(root, pre, ans);
        return ans;
    }
};