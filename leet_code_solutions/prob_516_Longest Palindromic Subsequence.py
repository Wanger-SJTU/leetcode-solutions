
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
		# print(memo)
		return memo[left][right]

	def DP_iter(self, s):
		lens = len(s)
		i = j = lens // 2
		memo = [[0 for i in range(len(s))] for j in range(len(s))]
		
		for i in range(lens-1, -1, -1):
			memo[i][i] = 1
			for j in range(i+1, lens):
				if s[i] == s[j]:
					memo[i][j] = memo[i+1][j-1]+2
				else:
					memo[i][j] = max(memo[i][j-1], memo[i+1][j])
			display(memo)
		return memo[0][-1]

	def __call__(self, s):
		return self.longestPalindromeSubseq(s)

def display(arr):
	print('-'*10)
	for row in arr:
		print(row)

if __name__ == '__main__':
	s = Solution()
	print(s.DP_iter('ssas'))