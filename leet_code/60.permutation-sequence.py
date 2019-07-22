#
# @lc app=leetcode id=60 lang=python3
#
# [60] Permutation Sequence
#
class Solution:
    def getPermutation(self, n: int, k: int) -> str:
        numbers = list(range(1, n+1))
        permutation = ''
        k -= 1
        while n > 0:
            n -= 1
            # get the index of current digit
            index, k = divmod(k, math.factorial(n))
            permutation += str(numbers[index])
            # remove handled number
            numbers.remove(numbers[index])

        return permutation


