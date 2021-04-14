/*
 * @lc app=leetcode.cn id=3 lang=cpp
 *
 * [3] 无重复字符的最长子串
 */
#include "leetcode.h"
// @lc code=start
class Solution
{
public:
  int lengthOfLongestSubstring(string s)
  {
    vector<int> dict(256, -1);
    int srt = -1;
    int len = 0;
    for (int i = 0; i < s.size(); i++) {
      if (dict[s[i]] > srt) {
        srt = dict[s[i]];
      }
      dict[s[i]] = i;
      len = max({len, i - srt});
    }
    return len;
  }
};
// @lc code=end
