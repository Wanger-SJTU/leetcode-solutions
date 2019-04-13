class Solution:
    def fangan_num(self,n):
        result =0
        #求只有n-5块巧克力的分配方式
        for i in range(1,n-5+1):
            result=result+self.gen_last_value(n-5-1,i-1)
        print(result)


    def get_value(self,n):
        if n == 1:
            return n
        if n==0:
            return 1
        else:
            return n * get_value(n - 1)

    def gen_last_value(self,n, m):
        first = self.get_value(n)

        second = self.get_value(m)

        third = self.get_value((n - m))

        return int(first / (second * third))


if __name__ =='__main__':
    # length = input()
    # arr = [int(x) for x in input().strip().split(' ')]

    #arr =[1,2,3,2,2,2,5,4,2]
    Solution().fangan_num(6)