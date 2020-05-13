/*
 * @lc app=leetcode.cn id=1201 lang=cpp
 *
 * [1201] 丑数 III
 */
#include "common.h"
// @lc code=start
#define LL long long
class Solution {
public:
  int nthUglyNumber(int n, int a, int b, int c) {
    LL low = min({a, b, c});
    LL hi = low * n;
    LL res = binSearch(low, hi, a, b, c, n);
    LL left_a = res % a;
    LL left_b = res % b;
    LL left_c = res % c;

    return res - min(left_a, min(left_b, left_c));
  }

private:
  LL binSearch(LL low, LL hi, int a, int b, int c, int n) {
    if (low >= hi)
      return low;
    LL mid = low + (hi - low) / 2;
    LL MCM_a_b = MCM(a, b);
    LL MCM_a_c = MCM(a, c);
    LL MCM_b_c = MCM(b, c);
    LL MCM_a_b_c = MCM(MCM_a_b, c);

    //????????????????a?b?c??????????a?b?c???????????????????
    // a?b?c????????
    LL count_n = mid / a + mid / b + mid / c - mid / MCM_a_b - mid / MCM_b_c -
                 mid / MCM_a_c + mid / MCM_a_b_c;
    if (count_n == n)
      return mid;
    if (count_n < n)
      return binSearch(mid + 1, hi, a, b, c, n);
    return binSearch(low, mid - 1, a, b, c, n);
  }
  //??????????????????
  LL MCM(LL a, LL b) {
    LL Multi = a * b;
    while (b > 0) {
      LL tmp = a % b;
      a = b;
      b = tmp;
    }
    return Multi / a;
  }
};
// @lc code=end
