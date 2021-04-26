/*
 * @lc app=leetcode.cn id=306 lang=cpp
 *
 * [306] 累加数
 */

#include "leetcode.h"

// @lc code=start
class Solution
{
public:
  bool isAdditiveNumber(string_view num)
  {

    auto twoSum = [](string num1, string num2) -> string {
      int i = num1.size() - 1, j = num2.size() - 1, s = 0;
      string ans;
      while (i >= 0 || j >= 0 || s) {
        s += (i >= 0 ? num1[i--] - '0' : 0) + (j >= 0 ? num2[j--] - '0' : 0);
        ans.insert(begin(ans), s % 10 + '0');
        s /= 10;
      }
      return ans;
    };

    const int n = num.length();
    vector<string> nums;
    function<bool(int)> dfs = [&](int p) {
      if (p == n) return nums.size() > 2;

      int max_len = num[p] == '0' ? 1 : n - p;
      for (int i = p; i < p + max_len; ++i) {
        string_view cur = num.substr(p, i - p + 1);
        if (nums.size() >= 2) {
          string sum = twoSum(nums.rbegin()[0], nums.rbegin()[1]);
          if (cur.compare(sum) > 0)
            break;  // pruning 剪枝
          else if (cur.compare(sum) < 0)
            continue;  // 继续扩展
          // cur must equals to sum
        }
        nums.emplace_back(cur);
        if (dfs(i + 1)) return true;
        nums.pop_back();  // backtracking 回溯
      }
      return false;
    };

    return dfs(0);
  }
};
// @lc code=end

int main()
{
  Solution s;
  string num = "";
  auto res = s.isAdditiveNumber(num);
  return res;
}
