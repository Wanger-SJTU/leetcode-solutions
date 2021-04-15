class Solution {
public:
    int computeArea(int A, int B, int C, int D, int E, int F, int G, int H) {
        int left_x = max(A,E);
        int left_y = max(B,F);
        int right_x = min(C,G);
        int right_y = min(D,H);
        int intersect_area = max(right_x - left_x,0)*max(right_y - left_y,0);
        return (C-A)*(D-B) + (G-E)*(H-F) - intersect_area;
    }
};