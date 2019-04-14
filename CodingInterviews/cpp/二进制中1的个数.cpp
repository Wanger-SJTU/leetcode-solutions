class Solution {
public:
     int  NumberOf1(int n) 
     {
         int count = 0;
         
         for(;n;++count)
         {
             n &= (n -1);
         }
         return count;
     }
};
/**/
