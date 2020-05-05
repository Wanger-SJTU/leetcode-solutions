/*
 * @lc app=leetcode.cn id=39 lang=cpp
 *
 * [39] 组合总和
 */
#include "common.h"
// @lc code=start
class Solution {
 public:
  vector<vector<int>> combinationSum(vector<int>& candidates, int target) {
    vector<vector<int>> res;
    sort(candidates.begin(), candidates.end());
    vector<int> tmp_res;
    search(candidates, 0, tmp_res, target, res);
    return res;
  }

 private:
  void search(vector<int>& candidates, int next_pos, vector<int>& tmp_res,
              int target, vector<vector<int>>& res) {
    if (target == 0) {
      res.push_back(tmp_res);
    }
    if (next_pos == candidates.size() || target - candidates[next_pos] < 0) {
      return;
    }
    tmp_res.push_back(candidates[next_pos]);
    search(candidates, next_pos, tmp_res, target - candidates[next_pos], res);
    tmp_res.pop_back();
    search(candidates, next_pos + 1, tmp_res, target, res);
  }
};
// @lc code=end
