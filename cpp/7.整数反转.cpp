/*
 * @lc app=leetcode.cn id=7 lang=cpp
 *
 * [7] 整数反转
 */
#include "leetcode.h"
// @lc code=start
class Solution
{
public:
  int reverse(int x)
  {
    string x_str = to_string(abs(x));
    std::reverse(x_str.begin(), x_str.end());
    long long res = stoll(x_str);
    if (x > 0) {
      return res > INT_MAX ? 0 : res;
    } else {
      return -1 * res < INT_MIN ? 0 : -1 * res;
    }
  }
};
// @lc code=end
