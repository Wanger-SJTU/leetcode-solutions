#include "leetcode.h"
class Solution {
public:
    string customSortString(string S, string T) {
        int arr[26] = {0};
        for (int i = 0; i < S.size(); ++i)
            arr[S[i] - 'a'] = i;
        sort(T.begin(), T.end(), [arr](const char& a, const char& b){
            return arr[a - 'a'] < arr[b - 'a'];
        });
        return T;
    }
};