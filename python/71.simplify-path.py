#
# @lc app=leetcode id=71 lang=python3
#
# [71] Simplify Path
#
class Solution:
    def simplifyPath(self, path: str) -> str:
        path = path.split('/')
        res = []
        for item in path:
            if item == '.':
               continue
            elif item == '..':
                if res:
                    res.pop(-1)
                continue
            elif not item:
                continue
            else:
                res.append(item)
        return '/'+'/'.join(res)    

if __name__ == "__main__":
    s = Solution()
    print(s.simplifyPath("/a//b////c/d//././/.."))
