/*
 * @lc app=leetcode.cn id=91 lang=cpp
 *
 * [91] 解码方法
 */
#include "leetcode.h"
// @lc code=start
class Solution
{
public:
  int numDecodings(string s)
  {
    int res = 0;
    // find(s, 0, res);
    return DpFind(s);
  }

private:
  // dfs TLE
  void find(string s, int srt, int& res)
  {
    if (srt >= s.size() - 1) {
      res += 1;
      cout << s.substr(0, srt) << endl;
      return;
    }
    // if (s[srt] == '0') {
    //   return;
    // }
    // find(s, srt + 1, res);
    // if (srt < s.size() - 1 && s[srt] == '1' ||
    //     (s[srt] == '2' && s[srt + 1] < '7')) {
    //   find(s, srt + 2, res);
    // }
  }

  int DpFind(string s)
  {
    int cnt = 0;
    if (s.size() == 0 || s[0] == '0') {
      return cnt;
    }
    if (s.size() == 1) {
      return 1;
    }
    vector<int> dp(s.size() + 1, 0);
    dp[0] = 1;
    for (int i = 0; i < s.size(); i++) {
      dp[i + 1] = s[i] == '0' ? 0 : dp[i];
      if (i > 0 && (s[i - 1] == '1' || (s[i - 1] == '2' && s[i] <= '6'))) {
        dp[i + 1] += dp[i - 1];
      }
    }
    return dp.back();
  }
};
// @lc code=end
