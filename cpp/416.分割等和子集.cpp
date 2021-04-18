#include "leetcode.h"
class Solution {
    bool helper(vector<int>& nums, int pos, int sum) {
        if (0 == sum) return true;
        if (sum < 0 || pos == nums.size()) return false;

        int ret = false;
        ret = helper(nums, pos + 1, sum - nums[pos]) ||
              helper(nums, pos + 1, sum);

        return ret;
    }
public:
    bool canPartition(vector<int>& nums) {
        int sum = 0;
        sum = accumulate(nums.begin(), nums.end(), 0);
        if (sum & 1) return false;
        sum >>= 1;
        sort(nums.rbegin(), nums.rend());
        if (nums[0] > sum) return false;
        return helper(nums, 0, sum);
    }
};