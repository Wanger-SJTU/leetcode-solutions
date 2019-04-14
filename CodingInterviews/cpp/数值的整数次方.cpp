class Solution {
public:
    
    double Power(double base, int exponent) 
    {
        double res = 1;
        int count;
        if(exponent<0)
        {
            count = -exponent;
            base = 1.0 / base;
        }
        else
        {
             count = exponent;
        }
        
        while(count > 0)
        {
            if(count%2==0)
            {
                res = res * res;
                count = count /2;
            }
            else
            {
                res = res*base;
                count--;
            }
        }
        return res;
    }
};