/*
 * @lc app=leetcode.cn id=783 lang=cpp
 *
 * [783] 二叉搜索树节点最小距离
 */

#include "leetcode.h"

/**
 * Definition for a binary tree node.
 */
struct TreeNode
{
  int val;
  TreeNode* left;
  TreeNode* right;
  TreeNode() : val(0), left(nullptr), right(nullptr) {}
  TreeNode(int x) : val(x), left(nullptr), right(nullptr) {}
  TreeNode(int x, TreeNode* left, TreeNode* right) : val(x), left(left), right(right) {}
};

// @lc code=start
class Solution
{
  void dfs(TreeNode* root, int& pre, int& ans)
  {
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

public:
  int minDiffInBST(TreeNode* root)
  {
    int ans = INT_MAX, pre = -1;
    dfs(root, pre, ans);
    return ans;
  }
};
// @lc code=end

int main() {}
