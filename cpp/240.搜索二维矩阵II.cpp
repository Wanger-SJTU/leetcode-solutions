class Solution {
public:
    bool searchMatrix(vector<vector<int>>& matrix, int target) {
        for(int i = 0; i < matrix.size(); ++i)
        {
            if(binarySearch(matrix, i, target))
                return true;
        }
        return false;
    }
    bool binarySearch(vector<vector<int>>& matrix, int i, int target)
    {
        int left = 0, right = matrix[0].size()-1;
        while(left <= right)
        {
            int mid = left + (right - left)/2;
            if(target > matrix[i][mid]) left = mid+1;
            else    if(target < matrix[i][mid])    right = mid-1;  
            else    return true; 

        }
        return false;
    }
};
