/*
 * @lc app=leetcode.cn id=34 lang=cpp
 *
 * [34] 在排序数组中查找元素的第一个和最后一个位置
 */
#include "common.h"
// @lc code=start
class Solution {
public:
  vector<int> searchRange(vector<int> &nums, int target) {
    int srt = 0, end = 0;
    int lo = 0, hi = nums.size() - 1;
    while (lo <= hi) {
      int mid = (hi - lo) / 2 + lo;
      if (nums[mid] == target) {
        srt = mid;
        end = mid;
        while (srt >= 0 && nums[srt] == target) {
          srt -= 1;
        }
        while (end < nums.size() && nums[end] == target) {
          end = end + 1;
        }
        return {srt + 1, end - 1};
      } else if (nums[mid] > target) {
        hi = mid - 1;
      } else {
        lo = mid + 1;
      }
    }
    return {-1, -1};
  }
};
// @lc code=end
