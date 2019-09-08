/*
 * @lc app=leetcode id=9 lang=cpp
 *
 * [9] Palindrome Number
 */
#include<string>
using namespace std;

class Solution {
public:
    bool isPalindrome(int x) {
        if(x<0)
            return false;
        string x_str = to_string(x);
        int i = 0, j = x_str.length()-1;
        while(i<=j)
        {
            if(x_str[i] != x_str[j])
                return false;
            i++;j--;
        }
        return true;
    }
};

