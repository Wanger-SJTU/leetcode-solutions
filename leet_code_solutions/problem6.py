
# problem description and solving ideas can be found in ./solutions/zigzag

class Solution(object):
    @staticmethod
    def convert(self, s, numRows):
        """
        :type s: str
        :type numRows: int
        :rtype: str
        """
        string = ""
        if numRows == 1:
            return s
        for idx in range(numRows):
            for j in range(len(s)):
                index = idx
                string += s(1, s[index])
                index = (2*numRows-2)*j +idx
