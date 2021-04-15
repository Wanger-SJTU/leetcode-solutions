class Solution {
public:
    int longestOnes(vector<int>& A, int K) {
        int l = 0, r = 0;
        while (r < A.size()) {
            if (A[r++] == 0) K--;
            if (K < 0 && A[l++] == 0) K++;
        }
        return r - l;
    }
};