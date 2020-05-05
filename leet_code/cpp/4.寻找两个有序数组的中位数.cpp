/*
 * @lc app=leetcode.cn id=4 lang=cpp
 *
 * [4] 寻找两个有序数组的中位数
 */
#include "common.h"
// @lc code=start
class Solution {
public:
  double findMedianSortedArrays(vector<int> &nums1, vector<int> &nums2) {
    if (nums1.size() > nums2.size()) {
      return findMedianSortedArrays(nums2, nums1);
    }
    int mid = (nums1.size() + nums2.size()) / 2;
  }
  int findKthElm(vector<int> &nums1, vector<int> &nums2, int k) {
    int le = max(0, int(k - nums2.size())), ri = min(k, int(nums1.size()));
    while (le < ri) {
      int m = le + (ri - le) / 2;
      if (nums2[k - m - 1] > nums1[m])
        le = m + 1;
      else
        ri = m;
    } //循环结束时的位置le即为所求位置，第k小即为max(nums1[le-1]),nums2[k-le-1])，但是由于le可以为0、k,所以
    // le-1或者k-le-1可能不存在所以下面单独判断下
    int nums1LeftMax = le == 0 ? INT_MIN : nums1[le - 1];
    int nums2LeftMax = le == k ? INT_MIN : nums2[k - le - 1];
    return max(nums1LeftMax, nums2LeftMax);
  }
};
// @lc code=end
