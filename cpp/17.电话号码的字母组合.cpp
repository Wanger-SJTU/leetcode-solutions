/*
 * @lc app=leetcode.cn id=17 lang=cpp
 *
 * [17] 电话号码的字母组合
 */
#include "leetcode.h"
// @lc code=start
class Solution
{
public:
  vector<string> letterCombinations(string digits)
  {
    if (digits.empty()) {
      return {};
    }
    vector<string> res = {""};
    vector<string> keymap = {"", "", "abc", "def", "ghi", "jkl", "mno", "pqrs", "tuv", "wxyz"};
    for (auto num : digits) {
      int n = res.size();
      for (auto chr : keymap[num - '0']) {
        for (int i = 0; i < n; ++i) {
          res.push_back(res[i] + chr);
        }
      }
      for (int i = 0; i < n; ++i) {
        res.erase(res.begin());
      }
    }
    return res;
  }
};
// @lc code=end
