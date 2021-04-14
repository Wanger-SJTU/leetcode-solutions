/*
 * @lc app=leetcode id=7 lang=cpp
 *
 * [7] Reverse Integer
 */
#include <climits>
using namespace std;

class Solution 
{
public:
    int reverse(int x) 
    {
        long res = 0;
        while(x)
        {
            res = res*10 + x % 10;
            x /= 10;
        }
        return (res > INT_MAX || res < INT_MIN) ? 0 : res;
    }
};

