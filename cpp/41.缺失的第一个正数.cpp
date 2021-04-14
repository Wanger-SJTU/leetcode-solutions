/*
 * @lc app=leetcode.cn id=41 lang=cpp
 *
 * [41] 缺失的第一个正数
 *
 * https://leetcode-cn.com/problems/first-missing-positive/description/
 *
 * algorithms
 * Hard (40.23%)
 * Likes:    668
 * Dislikes: 0
 * Total Accepted:    75.6K
 * Total Submissions: 188K
 * Testcase Example:  '[1,2,0]'
 *
 * 给你一个未排序的整数数组，请你找出其中没有出现的最小的正整数。
 * 
 * 
 * 
 * 示例 1:
 * 
 * 输入: [1,2,0]
 * 输出: 3
 * 
 * 
 * 示例 2:
 * 
 * 输入: [3,4,-1,1]
 * 输出: 2
 * 
 * 
 * 示例 3:
 * 
 * 输入: [7,8,9,11,12]
 * 输出: 1
 * 
 * 
 * 
 * 
 * 提示：
 * 
 * 你的算法的时间复杂度应为O(n)，并且只能使用常数级别的额外空间。
 * 
 */

#include "leetcode.h"
// @lc code=start
class Solution
{
public:
  int firstMissingPositive(vector<int>& nums)
  {
    for (int i = 0; i < nums.size(); i++) {
      if (i + 1 == nums[i]) continue;
      int x = nums[i];
      while (x >= 1 && x <= nums.size() && x != nums[x - 1]) {
        swap(x, nums[x - 1]);
      }
    }
    for (int i = 0; i < nums.size(); i++) {
      if (i + 1 != nums[i]) return i + 1;
    }
    return nums.size() + 1;
  }
};
// @lc code=end
