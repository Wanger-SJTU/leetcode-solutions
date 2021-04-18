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
class Solution
{
private:
  bool recur(TreeNode* root, int& height)
  {
    if (root == nullptr) {
      return true;
    }
    int left_height = 0;
    bool left_res = recur(root->left, left_height);
    if (left_res == false) {
      return false;
    }
    int right_height = 0;
    bool right_res = recur(root->right, right_height);
    if (right_res == false) {
      return false;
    }
    height = max({left_height, right_height}) + 1;
    return abs(left_height - right_height) < 2;
  }

public:
  bool isBalanced(TreeNode* root)
  {
    int height = 0;
    return recur(root, height);
  }
};