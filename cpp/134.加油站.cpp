class Solution {
public:
    int canCompleteCircuit(vector<int>& gas, vector<int>& cost) {
        int pos = 0;
        int curResidual = 0;
        int totalResidual = 0;
        for (int i = 0; i < gas.size(); ++i) {
            curResidual += (gas[i] - cost[i]);
            totalResidual += (gas[i] - cost[i]);
            if (curResidual < 0) {
                pos = i+1;
                curResidual = 0;
            }
        }
        return totalResidual < 0 ? -1 : pos;
    }
};