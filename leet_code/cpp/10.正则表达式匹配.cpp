/*
 * @lc app=leetcode.cn id=10 lang=cpp
 *
 * [10] 正则表达式匹配
 */
#include "common.h"
// @lc code=start
class Solution {
public:
  bool isMatch(string s, string p) {
    if (s.empty() || p.empty()) {
      return s.empty() && p.empty() ? true : false;
    }
    if (s[0] == p[0] || p[0] == '.') {
      return isMatch(s.substr(1, s.size()), p.substr(1, p.size()));
    } else if (p[0] == '*') {
      return isMatch(s, p.substr(1, s.size())) ||
             isMatch(s.substr(1, s.size()), p.substr(1, p.size())) ||
             isMatch(s.substr(1, s.size()), p);
    } else {
      return false || isMatch(s.substr(1, s.size()), p.substr(1, p.size())) ||
             isMatch(s, p.substr(1, p.size()));
    }
  }
};
// @lc code=end
//"aab"
//"c*a*b"