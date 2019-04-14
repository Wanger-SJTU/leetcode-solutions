
/*
题目描述
在一个二维数组中（每个一维数组的长度相同），
每一行都按照从左到右递增的顺序排序，每一列都按照从上到下递增的顺序排序。
请完成一个函数，输入这样的一个二维数组和一个整数，判断数组中是否含有该整数。
*/
#include <vector>
using namespace std;

class Solution 
{
public:
    bool Find(int target, vector<vector<int> > array) 
    {
        if (array.empty()) return false;
    
        int _length = array.size();
        for (int i = 0; i < _length; i++)
        {
            if (array[i].empty()) 
                continue;
            else if(target >= array[i][0])
            {
                if (target <= array[i][array[i].size() - 1])
                {
                    for (int j = array[i].size() - 1; j >= 0; j--)
                    {
                        if (target == array[i][j])return 1;
                        else if (target > array[i][j])break;
                    }
                }
                else {
                    continue;
                }
            }
            else return false;
        }
        return false;
        }
};