#
# @lc app=leetcode id=17 lang=python3
#
# [17] Letter Combinations of a Phone Number
#
class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        num2char = {
            '2':list('abc'),
            '3':list('def'),
            '4':list('ghi'),
            '5':list('jkl'),
            '6':list('mno'),
            '7':list('pqrs'),
            '8':list('tuv'),
            '9':list('wxyz')
        }
        res = []
        for idx,num in enumerate(digits):
            if idx == 0:
                res=num2char[num]
            else:
                tmp = []
                for item in res:
                    for char in num2char[num]:
                        tmp.append(item+char)
                res = tmp
        return res


