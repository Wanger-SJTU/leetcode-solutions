
class Solution:
    """
    @param l: the start range
    @param r: the end range
    @param k: the number of digits that should be different
    @return: the number of K-wolf numbers in range [l,r]
    """
    def getCount(self, l, r, k):
        # Write your code here.
        return count(r, k) - count(l-1,k)

    def count(n, k):
        if n < 10: return n
        rec = [int(i) for i in str(n)]
        cnt, t, n = 0, rec[0]-1, len(str(n))
        for i in range(1, len(str(n))):
            t *= max(10-i,10-k+1)

        cnt+=t
        for i in range(1, n+1):
            v = rec[i]-1
            m,j = v,i-1
            while j >= 0 and j >= i-k+1:
                if rec[j] <= v:
                    m -= 1
                j -= 1
            if m<-1: break
            if m >= 0:
                c=m+1
                for(int j=i+1;j<len;j++){
                    int a=Math.max(10-j,10-k+1);
                    c*=a;
                }
                cnt+=c;
            }
            for(int j=i-1;j>=0&&j>=i-k+1;j--){//检查是否有相同，有则停止
                if(rec[j]==rec[i]) break out;
            }

            if(i==len-1){//检查最后一位
                cnt++;
            }
        }
        return cnt+count((long)Math.pow(10.0,len-1)-1,k)

