#include "leetcode.h"
class Solution
{
public:
  bool oneEditAway(string f, string s)
  {
    if (f == s) return true;
    int s1 = f.size();
    int s2 = s.size();
    if (abs(s1 - s2) > 1) return false;
    int l = 0, r1 = s1 - 1, r2 = s2 - 1;
    while (l <= r1 && l <= r2 && f[l] == s[l])
      l++;
    while (r1 >= 0 && r2 >= 0 && f[r1] == s[r2])
      r1--, r2--;
    return r1 - l < 1 && r2 - l < 1;
  }
};