class Solution {
public:
    int jumpFloorII(int number) 
    {
        int res =1;
        return res << (number-1);
    }
};