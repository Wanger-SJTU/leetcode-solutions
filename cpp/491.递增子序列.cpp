#include "leetcode.h"
class Solution {
public:
    vector<vector<int>> findSubsequences(vector<int>& nums) {
        set<vector<int>> res;
        vector<vector<int>> resVector;
        if (nums.empty()) {
            return resVector;
        }
        for(int i = 0; i < nums.size() - 1; ++i) {
            findSubsequencesHelper(nums, i+1, {nums[i]}, res);
        }
        
        resVector.assign(res.begin(), res.end());
        return resVector ;
    }
    void findSubsequencesHelper(vector<int> nums, int srt, 
                vector<int> tmpRes, set<vector<int>>& res) {
        
        for(int i = srt; i < nums.size(); ++i) {
            if (nums[i] >= tmpRes[tmpRes.size()-1]) {
                tmpRes.push_back(nums[i]);
                res.insert(tmpRes);
                findSubsequencesHelper(nums, i+1, tmpRes, res);
                tmpRes.pop_back();
            }
        }
    }
};