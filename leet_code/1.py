from bisect import bisect_left
def calc(intervals):
    out = []
    if not intervals:
        print(0)
        return
    print(intervals[0][1]-intervals[0][0]+1)
    left = [intervals[0]]
    cur_sum = intervals[0][1]-intervals[0][0]+1
    
    for item in intervals[1:]:
        if item[0] >= left[-1][-1]:
            cur_sum += item[1]-item[0]+(item[0]!=left[-1][-1])
            print(cur_sum)
            if item[0] == left[-1][-1]:
                left[-1][-1] = item[1]
            else:
                left.append(item)
        elif item[1] <= left[0][0]:
            cur_sum += item[1]-item[0]+(item[1]!=left[0][0])
            print(cur_sum)
            if item[0] == left[-1][-1]:
                left[0][0] = item[0]
            else:
                left.insert(0, item)
        else:
            lo, hi = 0, len(left)
            found = False
            while lo < hi:
                mid = lo + (hi-lo)//2
                if left[mid][0] <= item[0] <= left[mid][1]:
                    found = True
                    if item[1] <= left[mid][1]:
                        print(cur_sum)
                    elif mid < len(left)-1 and item[1] >= left[mid+1][0]:
                        cur_sum += left[mid+1][0] - left[mid][1] -1
                        print(cur_sum)
                        left[mid][1] = left[mid+1][1]
                        left.pop(mid+1)
                    elif mid < len(left)-1 and item[1] < left[mid+1][0]:
                        cur_sum += item[1] - left[mid][1]
                        print(cur_sum)
                        left[mid][1] = item[1]
                    elif mid == len(left)-1:
                        cur_sum += item[1] - left[mid][1]
                        print(cur_sum)
                        left[mid][1] = item[1]  
                    break
                if left[mid][0] <= item[1] <= left[mid][1]:
                    found = True
                    if item[0] >= left[mid][0]:
                        print(cur_sum)
                    elif mid > 0 and item[0] <= left[mid-1][1]:
                        cur_sum += left[mid][0] - left[mid-1][1] -1
                        print(cur_sum)
                        left[mid-1][1] = left[mid][1]
                        left.pop(mid-1)
                    elif mid > 0 and item[0] > left[mid-1][1]:
                        cur_sum += left[mid][0] - item[0]
                        print(cur_sum)
                        left[mid][0] = item[0]
                    elif mid == 0:
                        cur_sum += left[mid][0] - item[0]
                        print(cur_sum)
                        left[mid][0] = item[0]  
                    break
                if left[mid][1] > item[0]:
                    lo = mid + 1
                elif left[mid][0] > item[1]:
                    hi = mid - 1

            if not found:
                idx = bisect_left(left, item)
                cur_sum += item[1]-item[0]+1
                print(cur_sum)
                left.insert(idx, item)

# if __name__ == "__main__":
#     n,m = map(int, input().split())
#     values = []
#     for _ in range(m):
#         values.append(list(map(int, input().split())))
#     calc(values)
print(calc([[1,2],[3,3],[4,4]]))

a = [[1,2],[1,3],[4,4]]
print(bisect_left(a, [2, 3]))