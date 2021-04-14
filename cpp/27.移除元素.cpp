/*
 * @lc app=leetcode.cn id=27 lang=cpp
 *
 * [27] 移除元素
 */
#include "leetcode.h"
// @lc code=start
class Solution
{
public:
  int removeElement(vector<int> &nums, int val)
  {
    if (nums.size() == 0) return 0;
    int slow = 0;
    int fast = 0;
    while (fast < nums.size()) {
      if (nums[fast] != val) {
        nums[slow++] = nums[fast++];
      } else {
        fast++;
      }
    }
    return slow;
  }
};
// @lc code=end
