/*
 * @lc app=leetcode.cn id=26 lang=cpp
 *
 * [26] 删除排序数组中的重复项
 */
#include "leetcode.h"
// @lc code=start
class Solution
{
public:
  int removeDuplicates(vector<int> &nums)
  {
    if (nums.size() <= 1) {
      return nums.size();
    }
    int slow = 0, fast = 1;
    while (fast < nums.size()) {
      if (nums[fast] == nums[slow]) {
        fast++;
      } else {
        nums[++slow] = nums[fast++];
      }
    }
    return slow + 1;
  }
};
// @lc code=end
