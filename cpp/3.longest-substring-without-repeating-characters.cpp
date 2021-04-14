/*
 * @lc app=leetcode id=3 lang=cpp
 *
 * [3] Longest Substring Without Repeating Characters
 */
// #include<string>
// using namespace std;
// #include<stdlib.h>
// #include<string.h>
class Solution {
public:
    int lengthOfLongestSubstring(string s) {
        int dict[256] = {0};
        memset(&dict, -1, 256*sizeof(int));
        int max_len = 0, srt = -1;
        for(int i = 0; i < s.length(); i++)
        {
            if(dict[s[i]] > srt)
                srt = dict[s[i]];
            dict[s[i]] = i;
            max_len= max(max_len, i-srt);
        }
        return max_len;
    }
};

