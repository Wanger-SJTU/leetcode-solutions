
# Given a string s, find the longest palindromic 
# subsequence's length in s. You may assume that
# the maximum length of s is 1000.

# Example 1:
# Input:

# "bbbab"
# Output:
# 4
# One possible longest palindromic subsequence is "bbbb".
# Example 2:
# Input:

# "cbbd"
# Output:
# 2
# One possible longest palindromic subsequence is "bb".

import pdb
class Solution:
	def longestPalindromeSubseq(self, s):
		"""
		:type s: str
		:rtype: int
		"""
		memo = [[None for i in range(len(s))] for j in range(len(s))]
		return self.__shrink(s, 0, len(s)-1, memo)

	def __shrink(self, s, left, right,  memo):
		if (memo[left][right] is not None):
			return memo[left][right]
		if (left > right):
			memo[left][right] = 0
			return 0
		if (left == right):
			memo[left][right] = 1
			return 1

		if (s[left] == s[right]):
			memo[left][right] = self.__shrink(s, left+1, right-1, memo) + 2
		else:
			memo[left][right] = max(self.__shrink(s, left+1, right, memo),\
															self.__shrink(s, left, right-1, memo))
		print(memo)
		return memo[left][right]

	def __call__(self, s):
		return self.longestPalindromeSubseq(s)
if __name__ == '__main__':
	s = Solution()
	print(s('ssas'))