/*
 * @lc app=leetcode.cn id=842 lang=cpp
 *
 * [842] 将数组拆分成斐波那契序列
 */
#include "leetcode.h"
// @lc code=start
using longint = long long int;
class Solution
{
public:
  vector<int> splitIntoFibonacci(string S)
  {
    vector<int> res;
    longint a1 = -1, a2 = -1;
    dfs(S, res, a1, a2);
    return res;
  }

private:
  bool IsValid(string str)
  {
    if (str[0] == '0') {
      return str.size() == 1;
    }
    return true;
  }
  bool dfs(string str, vector<int> &res, longint a, longint b)
  {
    if (str.size() == 0) {
      return res.size() >= 3;
    }
    longint val = 0;
    for (int i = 0; i < str.size(); i++) {
      try {
        val = std::stoi(str.substr(0, i + 1));
      } catch (const std::exception &e) {
        break;
      }

      if (IsValid(str.substr(0, i + 1)) && (val == a + b || (a == -1 || b == -1))) {
        res.push_back(val);
        if (dfs(str.substr(i + 1), res, b, val)) {
          return true;
        }
        res.pop_back();
      }
    }
    return false;
  }
};
// @lc code=end
