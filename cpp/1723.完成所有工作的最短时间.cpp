/*
 * @lc app=leetcode.cn id=1723 lang=cpp
 *
 * [1723] 完成所有工作的最短时间
 */

#include "leetcode.h"

// @lc code=start
class Solution {
public:
    int minimumTimeRequired(vector<int>& jobs, int k) 
    {
        sort(jobs.begin(), jobs.end(), greater<int>());
        int l = jobs[0];
        int r = accumulate(jobs.begin(), jobs.end(), 0);
        while (l < r) {
            auto mid = (r - l) / 2 + l;
            if (check(jobs, k, mid)) {
                r = mid;
            } else {
                l = mid + 1;
            }
        }
        return l;
    }
private:
    bool check(const vector<int>& jobs, int k, int limit)
    {
        vector<int> workloads(k, 0);
        return backtrace(jobs, workloads, 0, limit);
    }

    bool backtrace(const vector<int>& jobs, vector<int>& workloads, int idx, int limit)
    {
        //return condition
        if(idx >= jobs.size()) {
            return true;
        }
        //search
        for (auto& workload : workloads) {
            if (workload + jobs[idx] <= limit) {
                workload += jobs[idx];
                if (backtrace(jobs, workloads, idx + 1, limit)) {
                    return true;
                } 
                workload -= jobs[idx];
            }
            if (workload == 0 ) { //|| workload + jobs[idx] == limit) {
                break;
            }
        }
        return false;   
    }
};
// @lc code=end

int main()
{
    
}
