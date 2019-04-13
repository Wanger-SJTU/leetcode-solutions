class Solution:
    def isValid(self, s: str) -> bool:
        dic = {')':'(',']':'[','}':'{' }
        tmp = []
        for item in s:
            if item in dic.values():
                tmp.append(item)
            elif item in dic.keys():
                if len(tmp) == 0 or dic[item] != tmp[-1]:
                    return False
                else:
                    tmp.pop(-1)
        return True if len(tmp) == 0 else False

if __name__ == "__main__":
    s = Solution()
    print(s.isValid(']'))