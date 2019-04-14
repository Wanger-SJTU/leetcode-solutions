class Solution {
public:
    int rectCover(int number) 
    {
        int n1 =1, n2 = 2;
        if(number<=2) return number;
        int result = 0;
        while(number-->2)
        {
            result = n1+n2;
            n1 = n2;
            n2 = result;
        }
        return result;
    }
};