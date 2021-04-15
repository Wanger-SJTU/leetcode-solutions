#
# @lc app=leetcode id=66 lang=python3
#
# [66] Plus One
#
class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        flag = True
        for i in range(len(digits)-1, -1, -1):
            if flag:
                digits[i] = digits[i]+1
            if digits[i] > 9:
                digits[i] = digits[i]%10
                if i == 0:
                    digits.insert(0, 1)
            else:
                return digits
        return digits

