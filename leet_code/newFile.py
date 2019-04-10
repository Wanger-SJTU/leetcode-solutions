
def One_Pass(nums):
  max_sum, this_sum = 0,0
  s,e,ts=0,0,0
  for idx,num in enumerate(nums):
    this_sum =this_sum+num
    if this_sum <= 0:
        ts = idx+1
        e = idx+1
        this_sum = 0
    else:
        if this_sum > max_sum:
            s, e = ts, idx
            max_sum = this_sum
  return max_sum, s, e


values = [5,4,2,3]
# values = [-item for item in values]

res1 = One_Pass(values)
print(res1,values[res1[1]:res1[2]+1])