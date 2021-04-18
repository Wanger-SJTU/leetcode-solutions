#include "leetcode.h"
class Solution {
public:
    vector<int> majorityElement(vector<int>& nums) {
        if (nums.empty()) {
            return {};
        }

        int m = 0;
        int cm = 0;
        int n = 0;
        int cn = 0;
        for (const auto& num : nums) {
            if (m == num) {
                cm++;
            } else if (n == num) {
                cn++;
            } else if (cm == 0) {
                m = num;
                cm++;
            } else if (cn == 0) {
                n = num;
                cn++;
            } else {
                cm--;
                cn--;
            }
        }

        cm = 0;
        cn = 0;
        for (const auto& num : nums) {
            if (num == m) {
                cm++;
            } else if (num == n) {
                cn++;
            }
        }

        vector<int> res;
        if (cm > nums.size() / 3) {
            res.push_back(m);
        }
        if (cn > nums.size() / 3) {
            res.push_back(n);
        }
        return res;
    }
};
