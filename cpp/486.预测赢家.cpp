class Solution {
public:
    bool PredictTheWinner(vector<int>& nums) {
         vector<int> dp=nums;
        for(int i =nums.size()-2;i>=0; --i)
            for(int j=i+1;j<nums.size();++j){
               dp[j] = max(nums[i]-dp[j],nums[j]- dp[j-1]);
            }
        return dp.back()>=0;
    }
};