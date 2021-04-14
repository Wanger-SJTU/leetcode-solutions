/*
 * @lc app=leetcode.cn id=22 lang=cpp
 *
 * [22] 括号生成
 */
#include "leetcode.h"
// @lc code=start
class Solution
{
public:
  vector<string> generateParenthesis(int n)
  {
    vector<string> res;
    generate(n, n, "", res);
    return res;
  }

private:
  void generate(int l, int r, string cur, vector<string> &res)
  {
    if (l == 0 && r == 0) {
      res.push_back(cur);
    } else {
      if (l > 0) {
        generate(l - 1, r, cur + '(', res);
      }
      if (r > l) {
        generate(l, r - 1, cur + ')', res);
      }
    }
  }
};
// @lc code=end
