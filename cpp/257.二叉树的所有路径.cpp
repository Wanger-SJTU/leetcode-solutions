/*
 * @lc app=leetcode.cn id=257 lang=cpp
 *
 * [257] 二叉树的所有路径
 */

struct TreeNode
{
  int val;
  TreeNode* left;
  TreeNode* right;
  TreeNode(int x) : val(x), left(NULL), right(NULL) {}
};

#include "leetcode.h"
// @lc code=start

class Solution
{
public:
  vector<string> binaryTreePaths(TreeNode* root)
  {
    vector<string> v;
    if (root) preorder(v, root, "");
    return v;
  }
  void preorder(vector<string>& v, TreeNode* r, string t)
  {
    if (!r) return;
    if (!t.empty())
      t += ("->" + to_string(r->val));
    else
      t += to_string(r->val);
    if (r->left || r->right) {
      preorder(v, r->left, t);
      preorder(v, r->right, t);
    } else {
      v.push_back(t);
    }
  }
};
// @lc code=end
