/*
 * @lc app=leetcode.cn id=31 lang=cpp
 *
 * [31] 下一个排列
 */
#include "leetcode.h"
// @lc code=start
class Solution
{
public:
  void nextPermutation(vector<int> &nums)
  {
    int k = nums.size() - 2;
    int l = nums.size() - 1;
    while (k >= 0) {
      if (nums[k] < nums[k + 1]) {
        break;
      }
      k--;
    }
    if (k < 0) {
      reverse(nums.begin(), nums.end());
    } else {
      while (l > k) {
        if (nums[l] > nums[k]) {
          break;
        }
        l--;
      }
      swap(nums[k], nums[l]);
      reverse(nums.begin() + k + 1, nums.end());
    }
  }
};
// @lc code=end
