/*
 * @lc app=leetcode.cn id=102 lang=cpp
 *
 * [102] 二叉树的层序遍历
 */
#include "common.h"

// * Definition for a binary tree node.
struct TreeNode {
  int val;
  TreeNode *left;
  TreeNode *right;
  TreeNode(int x) : val(x), left(NULL), right(NULL) {}
};

// @lc code=start
class Solution {
public:
  vector<vector<int>> levelOrder(TreeNode *root) {
    vector<vector<int>> res;
    if (root == nullptr)
      return res;
    queue<TreeNode *> tmp_queue;
    tmp_queue.push(root);
    while (!tmp_queue.empty()) {
      int n = tmp_queue.size();
      vector<int> tmp_layer;
      while (n-- > 0) {
        auto node = tmp_queue.front();
        tmp_layer.push_back(node->val);
        tmp_queue.pop();
        if (node->left != nullptr) {
          tmp_queue.push(node->left);
        }
        if (node->right != nullptr) {
          tmp_queue.push(node->right);
        }
      }
      res.push_back(tmp_layer);
    }
    return res;
  }
};
// @lc code=end
