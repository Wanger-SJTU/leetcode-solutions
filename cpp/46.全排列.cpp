/*
 * @lc app=leetcode.cn id=46 lang=cpp
 *
 * [46] 全排列
 */
#include "leetcode.h"
// @lc code=start
class Solution
{
public:
  vector<vector<int>> permute(vector<int> &nums)
  {
    vector<vector<int>> res;
    vector<int> cur;
    permute_helper(nums, cur, res);
    return res;
  }

private:
  void permute_helper(vector<int> nums, vector<int> cur_res, vector<vector<int>> &res)
  {
    if (nums.empty()) {
      res.push_back(cur_res);
      return;
    }
    for (int i = 0; i < nums.size(); i++) {
      cur_res.push_back(nums[i]);
      nums.erase(nums.begin() + i);
      permute_helper(nums, cur_res, res);
      nums.insert(nums.begin() + i, cur_res[cur_res.size() - 1]);
      cur_res.pop_back();
    }
    return;
  }
};
// @lc code=end
