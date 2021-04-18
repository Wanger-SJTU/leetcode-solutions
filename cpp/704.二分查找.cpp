#include "leetcode.h"
/*
 * @lc app=leetcode.cn id=704 lang=cpp
 *
 * [704] 二分查找
 */
#include "leetcode.h"
// @lc code=start
class Solution
{
public:
  int search(vector<int> &nums, int target)
  {
    int lo = 0;
    int hi = nums.size() - 1;
    while (lo <= hi) {
      int mid = lo + (hi - lo) / 2;
      cout << mid << endl;
      if (nums[mid] == target) {
        return mid;
      } else if (nums[mid] > target) {
        hi = --mid;
      } else {
        lo = ++mid;
      }
    }
    return -1;
  }
};
// @lc code=end
