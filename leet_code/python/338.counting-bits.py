#
# @lc app=leetcode id=338 lang=python3
#
# [338] Counting Bits
#
class Solution:
    def countBits(self, num: int) -> List[int]:
        iniArr = [0]
        if num > 0:
            amountToAdd = 1
            while len(iniArr) < num + 1:
                iniArr.extend([x+1 for x in iniArr])
        
        return iniArr[0:num+1]


