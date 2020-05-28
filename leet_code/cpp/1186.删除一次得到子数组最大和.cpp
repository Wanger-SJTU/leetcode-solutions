/*
 * @lc app=leetcode.cn id=1186 lang=cpp
 *
 * [1186] 删除一次得到子数组最大和
 */
#include "common.h"
// @lc code=start
class Solution {
public:
  int maximumSum(vector<int> &arr) {
    if (arr.empty()) {
      return 0;
    }
    if (arr.size() == 1) {
      return arr[0];
    }
    vector<int> dp1(arr.size(), 0);
    vector<int> dp2(arr.size(), 0);
    dp1[0] = arr[0];
    for (int i = 1; i < arr.size(); i++) {
      dp1[i] = max(arr[i], dp1[i - 1] + arr[i]);
    }
    dp2[0] = arr[0];
    dp2[1] = max(arr[0], arr[1]);
    for (int i = 2; i < arr.size(); i++) {
      dp2[i] = max(dp1[i - 1], dp2[i - 1] + arr[i]);
    }
    int retCnt = INT_MIN;

    // 遍历以arr[i]为结尾，并且删除和不删除元素的情况，找出最大值！
    for (int i = 0; i < arr.size(); i++) {
      retCnt = max(dp1[i], retCnt);
      retCnt = max(retCnt, dp2[i]);
    }

    return retCnt;
  }
};
// @lc code=end
