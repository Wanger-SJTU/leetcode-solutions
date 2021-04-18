#include "leetcode.h"
int x = []() {
  std::ios::sync_with_stdio(false);
  cin.tie(NULL);
  return 0;
}();

class Solution
{
public:
  int findClosest(vector<string>& words, string word1, string word2)
  {
    int min = -1;
    int lastWord1Index = -1;
    int lastWord2Index = -1;
    for (int i = 0; i < words.size() - 1; i++) {
      if (words[i] == word1) {
        lastWord1Index = i;
      }
      if (words[i] == word2) {
        lastWord2Index = i;
      }

      if (lastWord1Index == -1 || lastWord2Index == -1) {
        continue;
      }

      int tmp = lastWord2Index > lastWord1Index ? lastWord2Index - lastWord1Index
                                                : lastWord1Index - lastWord2Index;
      if (tmp < min || min == -1) {
        min = tmp;
      }
    }

    return min;
  }
};