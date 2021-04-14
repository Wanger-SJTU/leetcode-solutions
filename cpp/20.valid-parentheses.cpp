/*
 * @lc app=leetcode id=20 lang=cpp
 *
 * [20] Valid Parentheses
 */
#include <stack>
#include <string>
#include <unordered_map>

using namespace std;

class Solution
{
public:
  bool isValid(string s)
  {
    stack<char> record;
    for (auto c : s) {
      switch (c) {
        case '(':
        case '[':
        case '{':
          record.push(c);
          break;
        case ')':
          if (record.empty() || record.top() != '(')
            return false;
          else
            record.pop();
          break;
        case ']':
          if (record.empty() || record.top() != '[')
            return false;
          else
            record.pop();
          break;
        case '}':
          if (record.empty() || record.top() != '{')
            return false;
          else
            record.pop();
          break;
        default:
          break;
      }
    }
    return record.empty();
  }
};
