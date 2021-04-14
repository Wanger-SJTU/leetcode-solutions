
# problem description and solving ideas can be found in ./solutions/restoreIpAddresses

class Solution(object):
    def restoreIpAddresses(self, s):
        """
        :type s: str
        :rtype: List[str]
        """
        # split the string into 4 part
        res = []
        self.getip(s, 4, "", res)
        return res

    def getip(self, s, k, out, result):
        if k == 0:
            if len(s) == 0:
                result.append(out)
        else:
            for i in range(4):
                if len(s) >= i and self._isValid(s[0:i]):
                    if k == 1:
                        self.getip(s[i:], k-1, out+s[0:i], result)
                    else:
                        self.getip(s[i:], k-1, out+s[0:i]+'.', result)
        return result
        
    def _isValid(self, s):
        if len(s) == 0 or len(s) > 3 or (len(s)>1 and s[0] =='0'):
            return False
        return 0 <= int(s) <= 255

if __name__ == '__main__':
    s = "25525511135"
    S = Solution()
    print(S.restoreIpAddresses(s))