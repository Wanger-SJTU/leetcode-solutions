/*
 * @lc app=leetcode.cn id=153 lang=cpp
 *
 * [153] 寻找旋转排序数组中的最小值
 */
#include "common.h"
// @lc code=start
class Solution {
public:
  int findMin(vector<int> &nums) {
    int l = 0, r = nums.size() - 1;
    while (l < r) {
      int mid = (r - l) / 2 + l;
      if (nums[mid] < nums[r]) {
        r = mid;
      } else {
        l = mid + 1;
      }
    }
    return nums[l];
  }
};
// @lc code=end
