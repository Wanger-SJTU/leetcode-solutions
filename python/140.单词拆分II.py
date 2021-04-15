import functools
class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> List[str]:
        if not s or not wordDict: return []
        
        n, word_dict = len(s), set(wordDict)
        
        max_len = max(map(len, word_dict))
        min_len = min(map(len, word_dict))

        @functools.lru_cache(None)
        def dp(i):
            if i >= n: return ['']
            res = []

            ed_left = i + min_len
            ed_right = min(i + max_len, n)

            for ed in range(ed_left, ed_right+1):
                if s[i:ed] in word_dict and dp(ed):
                    res += [s[i:ed] + ' ' + rest if rest else s[i:ed] for rest in dp(ed)]
                    
            return res
        
        return dp(0)