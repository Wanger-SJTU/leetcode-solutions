#include "leetcode.h"
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