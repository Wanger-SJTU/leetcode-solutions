class Solution:
    def longestValidParentheses(self, s: str) -> int:
        stack = [0]
        longest = 0
        for c in s:
            if c == '(':
                stack.append(0)
            else:
                if len(stack)>1:
                    val = stack.pop()
                    stack[-1] += (val + 2)
                    longest = max(longest, stack[-1])
                else:
                    stack = [0]
        return longest
    
    '''

    e.g.
     ( ( ) )
idx  0 1 2 3
dp 0 0 0 0 0
stk  0       i=0
     0 1     i=1
       p     i=2
dp 0 0 0 2
     p       i=3
dp 0 0 0 2 4

idea:
len = index[')'] - index[matched'('] +1
    '''
    def longestValidParentheses1(self, s: 'str') -> 'int':
        dp, stack = [0]*(len(s) + 1), []
        for i in range(len(s)):
            if s[i] == '(':
                stack.append(i)
            else:
                if stack:
                    p = stack.pop()
                    dp[i + 1] = dp[p] + i - p + 1
        return max(dp)