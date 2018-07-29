Given a string containing only digits, restore it by returning all possible valid IP address combinations.

**Example:**

```
Input: "25525511135"
Output: ["255.255.11.135", "255.255.111.35"]
```

给定一个字符串，输出所有可能的IP地址

## 递归求解

因为ip地址为4段，每段数值在`0-255`之间。从头开始，判断。只要满足每段在此范围内，即可进入下一段的操作。如果最后一段以后，长度为`0`。则此答案为正确答案。

```python
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
        """
        s ： input str
        out : result str
        result : all possible result
        k      : k-th part
        """
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
```



## DFS

