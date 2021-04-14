/*
 * @lc app=leetcode.cn id=274 lang=cpp
 *
 * [274] H 指数
 */

#include "leetcode.h"

// @lc code=start
class Solution
{
public:
  int hIndex(vector<int>& citations)
  {
    sort(citations.begin(), citations.end());
    int res = 0;
    for (int i = 0; i < citations.size(); ++i) {
      if (citations[i] >= citations.size() - i) {
        res = res < citations.size() - i ? citations.size() - i : res;
      }
    }
    return res;
  }
};
// @lc code=end

int main()
{
  Solution s;
  vector<int> case1 = {3, 0, 6, 1, 5};
  cout << s.hIndex(case1);
}
