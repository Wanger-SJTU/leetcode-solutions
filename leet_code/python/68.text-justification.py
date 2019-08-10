#
# @lc app=leetcode id=68 lang=python3
#
# [68] Text Justification
#
class Solution:
    def fullJustify(self, words: List[str], maxWidth: int) -> List[str]:
        res = []
        i = 0
        n = len(words)
        while i < n:
            j = i + 1
            wordsLen = len(words[i])
            while j < n and wordsLen + len(words[j]) + j - i <= maxWidth:
                wordsLen += len(words[j])
                j += 1
            tep = []
            blankLen = maxWidth - wordsLen
            if j == n or j == i + 1: # one word in a line or the last line
                for _ in range(i, j):
                    tep.append(words[_])
                    if _ != j - 1: tep.append(' ')
                s = ''.join(tep)
                res.append(s + (maxWidth - len(s)) * ' ')
            else: 
                numBlanks = j - i - 1
                for _ in range(i, j): # not the last line and more than one word in a line
                    tep.append(words[_])
                    if _ != j - 1: tep.append(' ' * (blankLen // (numBlanks) + (1 if _ - i < blankLen % (numBlanks) else 0)))
                res.append(''.join(tep))
            i = j
        return res

