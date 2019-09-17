from bisect import bisect_left
class Solution:
    """
    @param val: the personality value of user
    @return: Return their recommend friends' value
    """
    def getAns(self, val):
        # Write your code here
        if len(val) <= 1: return []
        res = []
        record = [val[0]]
        for i in range(1, len(val)):
            index = bisect_left(record, val[i])
            if index >= len(record):
                res.append(record[index-1])
            elif index == 0:
                res.append(record[index])
            else:
                tmp = [abs(record[index-1]-val[i]), abs(record[index]-val[i])]
                if index+1 < len(val):
                    tmp += [abs(record[index]-val[i])]
                res+= [record[index+tmp.index(min(tmp))-1]]
            record.insert(index, val[i])
        return res
if __name__ == "__main__":
    s = Solution()
    print(s.getAns([8,9,7,3,0,5,11]))
