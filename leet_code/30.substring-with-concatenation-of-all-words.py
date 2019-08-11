#
# @lc app=leetcode id=30 lang=python3
#
# [30] Substring with Concatenation of All Words
#
class Solution:
    def findSubstring(self, s: str, words: List[str]) -> List[int]:
        if len(words) == 0:return []
        l,d = len(words[0]),{}
        for w in words:
            d[w] = d.get(w, 0)+1
        i,ans = 0,[]

        for k in range(l):
            left, subd, count = k, {}, 0
            for j in range(k, len(s)-l+1, l):
                tword = s[j:j+l]
                # valid word
                if tword in d:
                    if tword in subd:
                        subd[tword] += 1
                    else:
                        subd[tword] = 1
                    count += 1
                    while subd[tword] > d[tword]:
                        subd[s[left:left+l]] -= 1
                        left += l
                        count -= 1
                    if count == len(words):
                        ans.append(left)
                # not valid
                else:
                    left = j + l
                    subd = {}
                    count = 0

        return ans    
