class Solution {
public:
    int findMinArrowShots(vector<vector<int>>& points) {
        if (points.size() <= 1) {
            return points.size();
        }
        sort(points.begin(), points.end(),
            [](const vector<int>& a, const vector<int>& b) { return a[0] == b[0] ? a[1] < b[1] : a[0] < b[0]; });
        
        int srt = points[0][0];
        int end = points[0][1];
        int res_cnt = 1;
        for (int i = 1; i < points.size(); ++i) {
            if (points[i][0] <= end) {
                end = min(points[i][1], end);
                srt = max(points[i][0], srt);
            }        else {
                res_cnt++;
                srt = points[i][0];
                end = points[i][1];
            }
        }
        return res_cnt;
    }
};