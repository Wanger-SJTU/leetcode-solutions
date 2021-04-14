/*
 * @lc app=leetcode.cn id=14 lang=cpp
 *
 * [14] 最长公共前缀
 */
#include "common.h"
// @lc code=start
class Solution {
public:
  string longestCommonPrefix(vector<string> &strs) {
    if (strs.empty())
      return "";
    string ans = "";
    sort(strs.begin(), strs.end());
    for (int i = 0;
         i < strs[0].size() && strs[0][i] == strs[strs.size() - 1][i]; ++i) {
      ans += strs[0][i];
    }
    return ans;
  }
};
// @lc code=end
