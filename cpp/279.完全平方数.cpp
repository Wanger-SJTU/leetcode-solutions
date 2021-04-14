/*
 * @lc app=leetcode.cn id=279 lang=cpp
 *
 * [279] 完全平方数
 */
#include "leetcode.h"
// @lc code=start
#include <cmath>
class Solution
{
public:
  int numSquares(int n)
  {
    vector<int> nums(n + 1, 1);
    nums[0] = 0;
    for (int i = 2; i <= n; i++) {
      int cur = INT_MAX;
      for (int j = 1; j <= sqrt(i); ++j) {
        cur = min(cur, 1 + nums[i - j * j]);
      }
      nums[i] = cur;
    }
    return nums[n];
  }
};
// @lc code=end
