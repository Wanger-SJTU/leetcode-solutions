#
# @lc app=leetcode id=30 lang=python3
#
# [30] Substring with Concatenation of All Words
#
from typing import List
from collections import Counter
class Solution:
    def findSubstring(self, s: str, words: List[str]) -> List[int]:
        if len(words) == 0:return []
        # initialize d, l, ans
        i,l,d,ans =0, len(words[0]), Counter(words),[]

        # sliding window(s)
        for k in range(l):
            left,subd,count = k,{},0
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
        
    def timeLimited(self, s: str, words: List[str]) -> List[int]:
        if not words or not s:
            return []
        max_len = max(map(len, words))
        srt, idx, words_dict = 0,0, Counter(words)
        res,changed,length = [],False,0
        while idx <= len(s)-max_len:
            for j in range(max_len):
                if s[idx:idx+j+1] in words_dict:
                    if words_dict[s[idx:idx+j+1]] > 0:
                        words_dict[s[idx:idx+j+1]] -= 1
                        if not changed:
                            changed = True
                            length = j
                            srt = idx
                        idx = idx+j+1    
                        break
                    else:
                        idx = srt + length +1
                        words_dict = Counter(words)
                        changed = False
                        break
            
            
            if sum(words_dict.values()) == 0:
                if sum(map(len,words)) == idx-srt:
                    res.append(srt)
                words_dict = Counter(words)
                changed = False
                idx = srt + length +1
            
        return res

if __name__ == "__main__":
    s = Solution()
    res = s.findSubstring("wordgoodgoodgoodbestword", ["word","good","best","good"])
    print(res)
