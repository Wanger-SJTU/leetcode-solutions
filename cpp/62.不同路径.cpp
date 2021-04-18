#include "leetcode.h"
class Solution {
public:
    int uniquePaths(int m, int n) {
      long long ans = 1;
        for (int x = n, y = 1; y < m; ++x, ++y) {
            ans = ans * x / y;
        }
        return ans;
    }
};