/*
 * @lc app=leetcode.cn id=420 lang=cpp
 *
 * [420] 强密码检验器
 */
#include "leetcode.h"
// @lc code=start
class Solution
{
public:
  int strongPasswordChecker(string s)
  {
    if (s.size() < 5) return 6 - s.size();
  }
};
// @lc code=end
