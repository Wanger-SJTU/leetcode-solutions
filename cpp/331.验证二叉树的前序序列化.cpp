#include "leetcode.h"
class Solution {
public:
    bool isValidSerialization(string preorder) {
        int n = preorder.size();
        int num = 0;//记录#的个数
          for(int i = n-1; i>=0;i--){
            if(preorder[i] == ',')
                continue;
            if(preorder[i] == '#')
                num++;
            else{
                while(i>=0 && preorder[i] != ',')//节点数字可能有多位
                    i--;
                if(num >= 2)//#的个数>=2，消除2个#，消除一个节点数字并转换成#，即num-1
                    num--;
                else
                    return false;//#的个数不足2，证明false
            }
        }
        if(num != 1)//最终#的个数须==1
            return false;
        return true;
    }
};