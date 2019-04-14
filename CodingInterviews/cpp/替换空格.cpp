class Solution {
public:
	void replaceSpace(char *str, int length) {
        if(str == NULL)
             return ;
        
        int count = 0;
        int len = 0;
        for(int idx =0; str[idx] != '\0'; idx++)
        {
            len += 1;
            if(str[idx]==' ') 
                count += 1;
        }
        
        for(int idx_src =len, idx_dst = len+count*2; idx_src >= 0; idx_src--)
        {
            if(str[idx_src] == ' ')
            {
                str[idx_dst--] = '0';
                str[idx_dst--] = '2';
                str[idx_dst--] = '%';
            }
            else
            {
                str[idx_dst--] = str[idx_src];
            }
        }
	}
};