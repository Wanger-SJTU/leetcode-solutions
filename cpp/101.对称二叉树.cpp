/*
 * @lc app=leetcode.cn id=101 lang=cpp
 *
 * [101] 对称二叉树
 */
#include "leetcode.h"
struct TreeNode
{
  int val;
  TreeNode *left;
  TreeNode *right;
  TreeNode(int x) : val(x), left(NULL), right(NULL) {}
};
// @lc code=start

// Definition for a binary tree node.
class Solution
{
public:
  bool isSymmetric(TreeNode *root)
  {
    if (root == nullptr) {
      return true;
    }
    return CheckSymmetric(root->left, root->right);
  }
  bool CheckSymmetric(TreeNode *left, TreeNode *right)
  {
    if (left == nullptr || right == nullptr) {
      return left == nullptr && right == nullptr;
    }
    if (left->val == right->val) {
      return CheckSymmetric(left->left, right->right) && CheckSymmetric(left->right, right->left);
    }
    return false;
  }
};
// @lc code=end
