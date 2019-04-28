
# Given a string, find the length of the longest substring without repeating characters.
# Examples:
# Given "abcabcbb", the answer is "abc", which the length is 3.
# Given "bbbbb", the answer is "b", with the length of 1.
# Given "pwwkew", the answer is "wke", with the length of 3. 
# Note that the answer must be a substring, "pwke" is a subsequence and not a substring.


class LengthOfLongestSubstring(object):
  
  def lengthOfLongestSubstring(self, s):
    """
    :type s: str
    :rtype: int
    """
    used = {}
    max_length = start = 0
    for i, c in enumerate(s):
      if c in used and start <= used[c]:
        start = used[c] + 1
      else:   
        max_length = max(max_length, i - start + 1)
      used[c] = i
    return max_length
 


  def bruteForce(self, s):
    '''
    This is the implementation to brute force method, but time limited
    '''
    ans = 0
    for i in range(len(s)):
      j = i+1
      while j < len(s):
        if self._unique(s, i, j):
          ans = max(ans, j-i+1)
    return ans

  def sliding_window(self,s):
    return lengthOfLongestSubstring(s)
  def _unique(self, s, start, end):
    set_char = set(list(s))
    return True if len(set_char) == len(s) else False

class Solution:
  def lengthOfLongestSubstring(self, s):
    b, m, d = 0, 0, {}
    for i, c in enumerate(s): 
      b, m, d[c] = max(b, d.get(c, -1) + 1), max(m, i - b), i
    return max(m, len(s) - b)



if __name__ == '__main__':
  s = LengthOfLongestSubstring()
  string = 'abcabacdbb'
  print(s.lengthOfLongestSubstring(string))
  print(func(string))
  #print(s.bruteForce(string))