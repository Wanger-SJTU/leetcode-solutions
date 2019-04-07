
# Given a string s, find the longest palindromic substring in s. 
# You may assume that the maximum length of s is 1000.
# 
# Example:
# Input: "babad"
# Output: "bab"
# Note: "aba" is also a valid answer.
# Example:
# Input: "cbbd"
# Output: "bb"
import pdb
_DEBUG = False
class Solution(object):
	def longestPalindrome(self, s):
		"""
		:type s: str
		:rtype: str
		"""
		pass
	def __DP_method(self, s):

		table = [[False for i in range(len(s))] for j in range(len(s))]
		sub_str = ""
		lens = 1
		while lens < len(s):
			for start in range(len(s)):
				end = start + lens -1
				if end >= len(s):
					break
				print(start, end)
				table[start][end] = (lens == 1 or lens == 2 or table[start+1][end-1]) \
						 and s[start] == s[end]
				if table[start][end] and len(sub_str) < end-start +1:
					sub_str = s[start:end+1]
			lens += 1
		for i in range(len(s)):
			print(table[i])
		return sub_str
	
def __expandAroundCenter(self,s):
	start = 0 
	end = 0
	for i in range(len(s)):
		len1 = self.__expand(s, i, i)
		len2 = self.__expand(s, i, i+1)
		max_len = max(len1,len2)
		
		if max_len >= end -start + 1:
			start = i - int((max_len - 1) // 2)
			end   = i + int(max_len // 2)
	return s[start:end + 1]

def __expand(self, s, left, right):
	L = left
	R = right
	while L >=0 and R < len(s) and s[L] == s[R]:
		L -= 1
		R += 1
	return R - L - 1

	def __call__(self, s, method='DP'):
		if _DEBUG:
			pdb.set_trace()
		values = {'DP': lambda x: self.__DP_method(x),
							'Expand':lambda x: self.__expandAroundCenter(x)
							}
		return values[method](s)


if __name__ == '__main__':
	s = Solution()
	input_ = "babad"
	print(s(input_))
	a= [[1,2,3]]*3

