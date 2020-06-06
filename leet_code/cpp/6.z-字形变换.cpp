/*
 * @lc app=leetcode.cn id=6 lang=cpp
 *
 * [6] Z 字形变换
 */
#include "common.h"
// @lc code=start
class Solution {
public:
  string convert(string s, int numRows) {
    if (numRows <= 1)
      return s;
    string res = "";
    int cycle = 2 * numRows - 2;
    for (int row = 0; row < numRows; ++row) {
      for (int j = row; j < s.size(); j += cycle) {
        res += s[j];
        int second = (j - row) + cycle - row;
        if (row != 0 && row != numRows - 1 && second < s.length())
          res = res + s[second];
      }
    }
    return res;
  }
};
// @lc code=end
