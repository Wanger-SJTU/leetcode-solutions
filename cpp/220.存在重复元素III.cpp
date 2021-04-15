class Solution {
public:
    bool containsNearbyAlmostDuplicate(vector<int>& nums, int k, int t) {
        std::set<long> s;
        for (int i = 0; i < nums.size(); ++i) {
            auto pos = s.lower_bound(long(nums[i])-t);
            ////< @attention
            if (pos!=s.end() && *pos<=long(nums[i])+t) 
            {
                return true;
            }
            s.insert(nums[i]);
            if (s.size() > k) 
            {
                s.erase(nums[i-k]);
            } ////< @note 维护活动窗口
        }
        return false;

    }
};