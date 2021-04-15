class Solution {
public:
    bool lemonadeChange(vector<int>& bills) {
       
    map<int, int> res = {{5, 0}, {10, 0}, {20, 0}};
    for (auto bill : bills) {
        if (bill == 5) {
            res[5]++;
        } else if (bill == 10) {
            if (res[5] ==0) {
                return false;
            }
            res[5]--;
            res[10]++;
        } else {
            if (res[5] > 0 && res[10] > 0) {
                    res[5]--;
                    res[10]--;
                } else if (res[5] >= 3) {
                    res[5] -= 3;
                } else {
                    return false;
                }
        }
    }
    return true;
    }
};