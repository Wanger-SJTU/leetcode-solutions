class Solution {
public:
    int minNumberInRotateArray(vector<int> rotateArray) {
      sort(rotateArray.begin(),rotateArray.end());
         
        return rotateArray[0];
    }
};