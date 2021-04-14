/*
 * @lc app=leetcode.cn id=287 lang=cpp
 *
 * [287] 寻找重复数
 */
#include "leetcode.h"
// @lc code=start
class Solution
{
public:
  int findDuplicate(vector<int>& nums)
  {
    int slow = 0, fast = 0, finder = 0;

    while (true) {
      slow = nums[slow];
      fast = nums[nums[fast]];
      if (slow == fast) {
        break;
      }
    }

    while (true) {
      finder = nums[finder];
      slow = nums[slow];

      if (finder == slow) {
        return finder;
      }
    }
  }
};
// @lc code=end
