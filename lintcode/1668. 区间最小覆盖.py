
#Definition of Interval.
class Interval(object):
    def __init__(self, start, end):
        self.start = int(start)
        self.end = int(end)

class Solution:
    """
    @param a: the array a
    @return: return the minimal points number
    """
    def getAns(self, a):
        # write your code here
        if not a: return 0
        a.sort(key=lambda x:x.start)
        idx,cnt = 1,len(a)
        srt,end = a[0].start, a[0].end
        while idx < len(a):
            if a[idx].start <= end:
                cnt -= 1
                end = min(end, a[idx].end)
            else:
                end = a[idx].end
            idx += 1
        return cnt

if __name__ == "__main__":
    s= Solution()
    with open("1688.in",'r') as f:
        line = f.readline().strip()[1:-1]
        items = line.split(')')
    values = [] 
    for item in items:
        i = item[2:].split(',')
        try:
            values.append(Interval(i[0], i[1]))
        except:
            continue

    print(s.getAns(values))