#include "leetcode.h"
class Solution
{
public:
  vector<int> smallestK(vector<int>& arr, int k)
  {
    vector<int> res;
    priority_queue<int> q;
    for (int a : arr) {
      q.push(a);
      if (q.size() > k) q.pop();
    }
    while (!q.empty()) {
      res.push_back(q.top());
      q.pop();
    }
    return res;
  }
};