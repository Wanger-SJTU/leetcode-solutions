/*
 * @lc app=leetcode.cn id=1011 lang=cpp
 *
 * [1011] 在 D 天内送达包裹的能力
 */

#include "leetcode.h"

// @lc code=start
class Solution
{
public:
  int shipWithinDays(vector<int>& weights, int D)
  {
    int lo = *max_element(weights.begin(), weights.end());
    int hi = accumulate(weights.begin(), weights.end(), 0);
    int day = 1;
    int cur = 0;
    while (lo < hi) {
      int mid = lo + (hi - lo) / 2;
      day = 1;
      cur = 0;
      for (const auto& w : weights) {
        if (cur + w > mid) {
          day++;
          cur = 0;
        }
        cur += w;
      }
      if (day <= D) {
        hi = mid;
      } else {
        lo = mid + 1;
      }
    }
    return lo;
  }
};
// @lc code=end

int main()
{
  vector<int> weights = {1, 2, 3, 4, 5, 6, 7, 8, 9, 10};
  Solution s;
  cout << s.shipWithinDays(weights, 5) << endl;
  ;
}
