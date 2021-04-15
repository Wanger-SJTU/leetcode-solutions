#
# @lc app=leetcode id=205 lang=python
#
# [205] Isomorphic Strings
#
class Solution(object):
    def isIsomorphic(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        s_dict,t_dict = {},{}
        for i,(s_chr,t_chr) in enumerate(zip(s,t)):
            if s_chr in s_dict and t_chr in t_dict:
                if s_dict[s_chr] != t_dict[t_chr]:
                    return False
                s_dict[s_chr] = s_dict.get(s_chr,[]) +[i]
                t_dict[t_chr] = t_dict.get(t_chr,[]) +[i]
            elif s_chr not in s_dict and t_chr not in t_dict:    
                s_dict[s_chr] = s_dict.get(s_chr,[]) +[i]
                t_dict[t_chr] = t_dict.get(t_chr,[]) +[i]
            else:
                return False
        return True
