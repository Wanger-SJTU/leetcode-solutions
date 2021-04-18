#include "leetcode.h"
class Solution {
public:
    int hIndex(vector<int>& citations) {
        int left=0;
        int right=citations.size();
        while(left<right){
            int mid=left+((right-left)>>1);
            if(citations[mid]<(int)citations.size()-mid){
                left=mid+1;
            }
            else{
                right=mid;
            }
        }
        return citations.size()-left;
    }
};