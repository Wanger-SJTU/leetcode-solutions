#
# @lc app=leetcode id=190 lang=python
#
# [190] Reverse Bits
#
class Solution:
    # @param n, an integer
    # @return an integer
    def reverseBits(self, n):
        oribin='{0:032b}'.format(n)
        reversebin=oribin[::-1]
        return int(reversebin,2)


