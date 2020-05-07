/*
 * @lc app=leetcode.cn id=44 lang=cpp
 *
 * [44] 通配符匹配
 */
#include "common.h"
// @lc code=start
class Solution {
public:
  bool isMatch(string s, string p) {
    if (p.empty()) {
      return s.empty();
    }
    if (p[0] == '*') {
      if (s.empty()) {
        return isMatch(s, p.substr(1, p.size()));
      } else {
        return isMatch(s.substr(1, s.size()), p.substr(1, p.size())) ||
               isMatch(s.substr(1, s.size()), p) ||
               isMatch(s, p.substr(1, p.size()));
      }

    } else {
      bool frist = !s.empty() && (s[0] == p[0] || p[0] == '?');
      return frist && isMatch(s.substr(1, s.size()), p.substr(1, p.size()));
    }
  }
};
// @lc code=end
