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
    vector<int> RobInternal(TreeNode* node) {
        if (node == nullptr) {
            return {0, 0};
        }
        auto l = RobInternal(node->left);
        auto r = RobInternal(node->right);
        int selected = node->val + l[0] + r[0];
        int notSelected = max(l[0], l[1]) + max(r[0], r[1]);
        return {notSelected, selected};
    }
    int rob(TreeNode* root) {
        auto res = RobInternal(root);
        return res[0] > res[1] ? res[0] : res[1];
    }
};