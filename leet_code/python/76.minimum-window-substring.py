#
# @lc app=leetcode id=76 lang=python3
#
# [76] Minimum Window Substring
#
from collections import Counter

class Solution:
    def minWindow(self, s: str, t: str) -> str:
        target_count_dict = Counter(t)
        remain_missing = len(t)
        start_pos, end_pos = 0, float('inf')
        current_start = 0
        
        # Enumerate function makes current_end indexes from 1
        for current_end, ch in enumerate(s, 1):
            # Whenever we encounter a character, no matter ch in target or not, we minus 1 in count dictionary
            # But, only when ch is in target, we minus the length of remain_missing
            # When the remain_missing is 0, we find a potential solution.
            if target_count_dict[ch] > 0:
                remain_missing -= 1
            target_count_dict[ch] -= 1
            
            if remain_missing == 0:
                # Remove redundant character
                # Try to find the fist position in s that makes target_count_dict value equals 0
                # Which means we can't skip this character in s when returning answer
                while target_count_dict[s[current_start]] < 0:
                    target_count_dict[s[current_start]] += 1
                    current_start += 1
                if current_end - current_start < end_pos - start_pos:
                    start_pos, end_pos = current_start, current_end
                
                # We need to add 1 to current_start, and the correspondence value in dictionary, is because
                # this is the first character of the potential answer. So, in future iteration, when we encounter this character,
                # We can remove this currently first character to try to find a shorter answer.
                target_count_dict[s[current_start]] += 1
                remain_missing += 1
                current_start += 1
        
        return s[start_pos:end_pos] if end_pos != float('inf') else ""

    def funcname(self, parameter_list):
        need, missing = collections.Counter(t), len(t)
        i = I = J = 0
        for j, c in enumerate(s, 1):
            missing -= need[c] > 0
            need[c] -= 1
            if not missing:
                while i < j and need[s[i]] < 0:
                    need[s[i]] += 1
                    i += 1
                if not J or j - i <= J - I:
                    I, J = i, j
        return s[I:J]

