#
# @lc app=leetcode.cn id=354 lang=python3
#
# [354] 俄罗斯套娃信封问题
#
from bisect import bisect_left
class Solution:
    def maxEnvelopes(self, envelopes: List[List[int]]) -> int:
        if not envelopes:
            return 0

        res, n = 0, len(envelopes)
        envelopes.sort(key=lambda a:(a[0], -a[1]))
        mem = list()
        for e in envelopes:
            index = bisect_left(mem, e[1])
            if len(mem) == index:
                mem.append(e[1])
            else:
                mem[index] = e[1]
        return len(mem)

    def maxEnvelopesDP(self, envelopes: List[List[int]]) -> int:
        if not envelopes:
            return 0

        res, n = 0, len(envelopes)
        envelopes.sort(key=lambda a:a[0])
        mem = [1]*n
        for i in range(n):
            for j in range(i):
                if envelopes[i][0] > envelopes[j][0] and envelopes[i][1] > envelopes[j][1]:
                    mem[i] = max(mem[j]+1, mem[i])
            res = max(res, mem[i])
        return res

