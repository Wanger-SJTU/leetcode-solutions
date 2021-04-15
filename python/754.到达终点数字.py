#
# @lc app=leetcode id=754 lang=python3
#
# [754] Reach a Number
#
import math

class Solution:
    def reachNumber1(self, target: int) -> int:
        target,step = abs(target),0
        while target > 0:
            step += 1
            target -= step
        return step if target % 2 == 0 else step + 1 + step%2

    def reachNumber(self, target: int) -> int:
        target,step = abs(target),0
        while target - (step+1)*step / 2 > 0  or target&1 != step*(step+1)//2&1:
            #     break
            #print(step)
            step += 1
        return step
# 思路：
# 1. target 正负号不影响结果
# 2. 假设所有的step都向右的和为s，这时转换一个数字n向左，即减去这个数字的两倍（s - 2 * n）
# 3. 最多只有一个数字向左，即可达到target
# 4. 因为 s 需要减去一个偶数2*n，所以target 与 s 必须同为偶数，或者奇数
# 5. 完成

    def reachNumber2(self, target):
        target = abs(target)
        n = int(math.ceil(math.sqrt(1 + 8 * target)/2 - 0.5))  # 一元二次方程的解
        while target % 2 != n * ( n + 1 ) / 2 % 2:  # 同为奇数/偶数
            n += 1
        return n

if __name__ == "__main__":
    s = Solution()
    # for i in range(1,100):
    res =s.reachNumber(8)
    print(res)
