/*
 * @lc app=leetcode id=1 lang=cpp
 *
 * [1] Two Sum
 */

#include <iostream>
#include <vector>
#include <map>
#include <algorithm>
using namespace std;

// @lc code=start
class Solution 
{
public:
    vector<int> twoSum(vector<int>& nums, int target) 
    {
        map<int, int> record;
        vector<int> res;
        for(auto i = 0; i < nums.size(); i++)
        {
            if(record.find(target-nums[i]) != record.end())
            {
                return {i, record[target-nums[i]]};
            }
            record[nums[i]] = i;
        }
        return res;
    }
};

// @lc code=end

