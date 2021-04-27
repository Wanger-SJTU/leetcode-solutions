/*
 * @lc app=leetcode.cn id=938 lang=cpp
 *
 * [938] 二叉搜索树的范围和
 */

#include "leetcode.h"

// 
//  * Definition for a binary tree node.
struct TreeNode {
    int val;
    TreeNode *left;
    TreeNode *right;
    TreeNode() : val(0), left(nullptr), right(nullptr) {}
    TreeNode(int x) : val(x), left(nullptr), right(nullptr) {}
    TreeNode(int x, TreeNode *left, TreeNode *right) : val(x), left(left), right(right) {}
};
//  */
// @lc code=start
class Solution {
public:
    int rangeSumBST(TreeNode* root, int low, int high) {
        int res = 0;
        inorder(root, low, high, res);
        return res;
    }
private:
    void inorder(TreeNode* root, int low, int high, int& sum) {
        if(root == nullptr) {
            return;
        }
        if (root->val >= low)
            inorder(root->left, low, high, sum);
        if (root->val >= low && root->val <= high)
            sum+= root->val;
        if (root->val <= high)
            inorder(root->right, low, high, sum);
    }
};
// @lc code=end

int main()
{
    Solution s;

}
