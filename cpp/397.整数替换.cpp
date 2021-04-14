/*
 * @lc app=leetcode.cn id=397 lang=cpp
 *
 * [397] 整数替换
 */
#include "leetcode.h"
// @lc code=start
class Solution
{
public:
  int integerReplacement(int n)
  {
    if (n == 1) {
      return 0;
    }
    if (n == 3) {
      return 2;
    }
    if (n == INT_MAX) return 32;
    if ((n & 1) == 0) {
      return 1 + integerReplacement(n >> 1);
    } else {
      return (n + 1) % 4 == 0 ? 1 + integerReplacement(n + 1) : 1 + integerReplacement(n - 1);
    }
  }
};
// @lc code=end
