# 40 ms, faster than 99.82% 
class Solution:
    def addDigits(self, num: int) -> int:
        num = str(num)
        while len(num)>1:
            num = sum(int(i) for i in num)
            num = str(num)
        return int(num)
# O(1)
class Solution:
    def addDigits(self, num: int) -> int:
        return 1 + (num - 1) % 9 if num !=0 else 0