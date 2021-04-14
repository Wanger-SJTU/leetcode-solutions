/*
 * @lc app=leetcode.cn id=1402 lang=cpp
 *
 * [1402] 做菜顺序
 */
#include "leetcode.h"
// @lc code=start
class Solution
{
public:
  int maxSatisfaction(vector<int> &satisfaction)
  {
    sort(satisfaction.begin(), satisfaction.end());
    int Cumulative_sum = 0;

    int ans = 0;
    int cur = 0;
    for (int i = satisfaction.size() - 1; i >= 0; i--) {
      cur += Cumulative_sum + satisfaction[i];
      Cumulative_sum += satisfaction[i];
      ans = max(ans, cur);
    }
    return ans;
  }
};
// @lc code=end
