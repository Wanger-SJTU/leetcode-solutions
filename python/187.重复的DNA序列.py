#
# @lc app=leetcode id=187 lang=python3
#
# [187] Repeated DNA Sequences
#
class Solution:
    def findRepeatedDnaSequences(self, s: str) -> List[str]:
        sequences = collections.defaultdict(int) #set '0' as the default value for non-existing keys
        for i in range(len(s)-9):
            sequences[s[i:i+10]] += 1#add 1 to the count
        return [key for key, value in sequences.items() if value > 1] #extract the relevant keys


