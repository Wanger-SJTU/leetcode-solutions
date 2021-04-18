#include "leetcode.h"
class Solution
{
public:
  string sortString(string s)
  {
    vector<char> count(26, 0);
    for (auto& a : s) {
      count[a - 'a']++;
    }
    string res;
    while (total > 0) {
      for (int i = 0; i < 26; ++i) {
        if (count[i] > 0 && total > 0) {
          count[i]--;
          res += (i + 'a');
          total--;
        }
      }
      for (int i = 25; i >= 0; --i) {
        if (count[i] > 0 && total > 0) {
          count[i]--;
          res += (i + 'a');
          total--;
        }
      }
    }
    return res;
  }
};