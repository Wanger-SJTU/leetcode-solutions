/*
 * @lc app=leetcode.cn id=241 lang=cpp
 *
 * [241] 为运算表达式设计优先级
 */

#include "leetcode.h"

// @lc code=start
class Solution
{
public:
  vector<int> diffWaysToCompute(string expression)
  {
    vector<int> ways;
    for (int i = 0; i < expression.length(); ++i) {
      char c = expression[i];
      if (c == '+' || c == '-' || c == '*') {
        vector<int> left = diffWaysToCompute(expression.substr(0, i));
        vector<int> right = diffWaysToCompute(expression.substr(i + 1));
        for (int i : left) {
          for (int j : right) {
            switch (c) {
              case '+':
                ways.push_back(i + j);
                break;
              case '-':
                ways.push_back(i - j);
                break;
              case '*':
                ways.push_back(i * j);
                break;
            }
          }
        }
      }
    }
    if (ways.empty()) ways.push_back(stoi(expression));
    return ways;
  }
};
// @lc code=end

int main()
{
  Solution s;
  s.diffWaysToCompute("2-1-1");
}
