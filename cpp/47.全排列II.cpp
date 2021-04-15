class Solution {

public:
    vector<vector<int>> permuteUnique(vector<int> &nums) {
        vector<vector<int>> res;
        sort(nums.begin(), nums.end());
        permute_helper(nums, 0, nums.size(), res);
        return res;
    }

private:
    void permute_helper(vector<int> nums, int srt, int end,
                        vector<vector<int>> &res) {
        if (srt == end - 1) {
        res.push_back(nums);
        return;
        }
        for (int i = srt; i < end; i++) {
        if (i != srt && nums[i] == nums[srt])
            continue;
        swap(nums[i], nums[srt]);
        permute_helper(nums, srt + 1, end, res);
        }
        return;
    }
};