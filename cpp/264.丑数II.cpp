#include "leetcode.h"
class Solution
{
public:
  int nthUglyNumber(int n)
  {
    vector<int> factors = {2, 3, 5};
    unordered_set<long> seen;
    priority_queue<long, vector<long>, greater<long>> heap;
    seen.insert(1L);
    heap.push(1L);
    int ugly;
    for (int i = 0; i < n; ++i) {
      long cur = heap.top();
      heap.pop();
      ugly = (int)cur;
      for (int factor : factors) {
        long next = cur * factor;
        if (!seen.count(next)) {
          seen.insert(next);
          heap.push(next);
        }
      }
    }
    return ugly;
  }
};