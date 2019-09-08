#
# @lc app=leetcode.cn id=165 lang=python3
#
# [165] 比较版本号
#
class Solution:
    def compareVersion(self, version1: str, version2: str) -> int:
        version1 = list(map(int, version1.split('.')))
        version2 = list(map(int, version2.split('.')))
        for idx, (a,b) in enumerate(zip(version1, version2)):
            if a > b:
                return 1
            elif a < b:
                return -1

        if len(version1) == len(version2):
            return 0
        elif len(version1) > len(version2):
            return 1  if sum(version1[idx+1:]) != 0 else 0
        else:
            return -1 if sum(version2[idx+1:]) != 0 else 0

if __name__ == "__main__":
    s = Solution()
    print(s.compareVersion("1","1.1"))
