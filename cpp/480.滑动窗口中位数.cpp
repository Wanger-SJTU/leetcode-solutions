/*
 * @lc app=leetcode.cn id=480 lang=cpp
 *
 * [480] 滑动窗口中位数
 */

#include "leetcode.h"

// @lc code=start
class Solution
{

private:
  priority_queue<int> small;
  priority_queue<int, vector<int>, greater<int> > big;
  unordered_map<int, int> mp;
  double get(int& k)
  {
    if (k % 2)
      return small.top();
    else
      return ((long long)small.top() + big.top()) * 0.5;
  }

public:
  vector<double> medianSlidingWindow(vector<int>& nums, int k)
  {
    for (int i = 0; i < k; i++) {
      small.push(nums[i]);
    };
    for (int i = 0; i < k / 2; i++) {
      big.push(small.top());
      small.pop();
    }
    vector<double> ans{get(k)};
    for (int i = k; i < nums.size(); i++) {
      int balance = 0;
      int l = nums[i - k];
      mp[l]++;
      if (!small.empty() && l <= small.top()) {
        balance--;
      } else {
        balance++;
      }
      if (!small.empty() && nums[i] <= small.top()) {
        small.push(nums[i]);
        balance++;
      } else {
        big.push(nums[i]);
        balance--;
      }
      if (balance > 0) {
        big.push(small.top());
        small.pop();
      }
      if (balance < 0) {
        small.push(big.top());
        big.pop();
      }
      while (!small.empty() && mp[small.top()] > 0) {
        mp[small.top()]--;
        small.pop();
      }
      while (!big.empty() && mp[big.top()] > 0) {
        mp[big.top()]--;
        big.pop();
      }
      ans.push_back(get(k));
    }
    return ans;
  }
};
// @lc code=end

int main() {}
