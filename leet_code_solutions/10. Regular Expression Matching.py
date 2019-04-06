

'''
递归：
'''
# 没有 * 的递归解法
# 从左往右匹配

def match(text, pattern):
    if not pattern: 
        return not text
    first_match = bool(text) and pattern[0] in {text[0], '.'}
    return first_match and match(text[1:], pattern[1:])

# 有 * 的递归解法
# 如果下一个是 * 匹配的结果是 当前匹配的结果-
# first_match && src[1:] 与pattern（匹配*） && src 与 pattern[2:] (*匹配结束)
def isMatch(text:str, pattern:str)->bool:
    if not pattern:
        return not text
    first_match = bool(text) and pattern[0] in {text[0], '.'}
    if len(pattern) >= 2 and pattern[1] == '*':
        return (self.isMatch(text, pattern[2:]) or
                first_match and self.isMatch(text[1:], pattern))
    else:
        return first_match and self.isMatch(text[1:], pattern[1:])

'''
Dynamic Programming
i :--> src
j :--> pattern

F[i,j] = {
    F[i-1,j-1] and match(s[i],p[j])  if p[j] !=  '*'
    F[i+1,j]  or F[i,j+2] and match(s[i],p[j])  if p[j] ==  '*'
}

'''


def dpMatch(text, pattern):
    dp = [[False] * (len(pattern) + 1) for _ in range(len(text) + 1)]
    dp[-1][-1] = True
    for i in range(len(text), -1, -1):
        for j in range(len(pattern) - 1, -1, -1):
            first_match = i < len(text) and pattern[j] in {text[i], '.'}
            if j+1 < len(pattern) and pattern[j+1] == '*':
                dp[i][j] = dp[i][j+2] or first_match and dp[i+1][j]
            else:
                dp[i][j] = first_match and dp[i+1][j+1]

    return dp[0][0]



if __name__ == "__main__":
    pass