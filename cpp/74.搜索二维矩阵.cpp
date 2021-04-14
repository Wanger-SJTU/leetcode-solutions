/*
 * @lc app=leetcode.cn id=74 lang=cpp
 *
 * [74] 搜索二维矩阵
 */
#include "leetcode.h"
// @lc code=start
class Solution
{
public:
  bool searchMatrix(vector<vector<int>>& matrix, int target)
  {
    int low = 0;
    int hi = matrix.size();
    int mid = low + (hi - low) / 2;
    while (matrix[mid][0] <= target && matrix[mid][0] >= target) {
    }
  }
};
// @lc code=end
