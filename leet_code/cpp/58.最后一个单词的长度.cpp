/*
 * @lc app=leetcode.cn id=58 lang=cpp
 *
 * [58] 最后一个单词的长度
 */
#include "common.h"
// @lc code=start
class Solution {
public:
  int lengthOfLastWord(string s) {
    if (s.empty()) {
      return 0;
    }
    int i = s.size() - 1;
    while (s[i] == ' ' && i > 0) {
      i--;
    }
    if (i < 0)
      return 0;
    int j = i;
    for (; j >= 0 && s[j] != ' '; --j) {
    }
    return i - j;
  }
};
// @lc code=end
