class Solution {
public:
  int rob(vector<int> &nums) {
    if (nums.size() < 2)
      return nums.size() == 0 ? 0 : nums[0];
    int res1 = 0;
    int res2 = 0;
    int pre2 = 0;
    int pre1 = 0;
    for (int i = 0; i < nums.size() - 1; i++) {
      int cur = max({pre2 + nums[i], pre1});
      pre2 = pre1;
      pre1 = cur;
    }
    res1 = pre1;
    pre2 = 0;
    pre1 = 0;
    for (int i = 1; i < nums.size(); i++) {
      int cur = max({pre2 + nums[i], pre1});
      pre2 = pre1;
      pre1 = cur;
    }
    return max({res1, pre1});
  }
};