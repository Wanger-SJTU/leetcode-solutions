class Solution {
public:
    int maxSubArray(vector<int>& nums) {
         int sz = nums.size();
        vector<int> dp(sz+1, 1);
        dp[0] = 0; // 表示没有元素
        int ret = nums[0];
        for (int i=1; i<=sz; ++i) {
            dp[i] = max(nums[i-1], dp[i-1]+nums[i-1]);
            ret = max(ret, dp[i]);
        }
        return ret;
    }
};