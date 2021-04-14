/*
 * @lc app=leetcode.cn id=470 lang=cpp
 *
 * [470] 用 Rand7() 实现 Rand10()
 */
#include "leetcode.h"
// The rand7() API is already defined for you.
extern int rand7();
// @return a random integer in the range 1 to 7
// @lc code=start

class Solution
{
public:
  int rand10()
  {
    int a, b, idx;
    while (true) {
      a = rand7();
      b = rand7();
      idx = b + (a - 1) * 7;

      if (idx <= 40) {
        return 1 + (idx - 1) % 10;
      }
      a = idx - 40;
      b = rand7();

      // get uniform dist from 1 - 63
      idx = b + (a - 1) * 7;

      if (idx <= 60) {
        return 1 + (idx - 1) % 10;
      }

      a = idx - 60;
      b = rand7();
      // get uniform dist from 1 - 21
      idx = b + (a - 1) * 7;

      if (idx <= 20) {
        return 1 + (idx - 1) % 10;
      }
    }
  }
};
// @lc code=end
