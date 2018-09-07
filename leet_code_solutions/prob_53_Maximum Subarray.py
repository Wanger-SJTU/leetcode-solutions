

def brute_force(nums):
  max_sum = 0 
  for L in range(len(nums)):
    for R in range(L,len(nums)):
      cur_sum = 0
      for i in range(L,R):
        cur_sum+=nums[i]
        if cur_sum > max_sum:
          max_sum = cur_sum
  return max_sum

def Devided_Conquer(nums, left, right):
  if left == right:
    return nums[left] #if nums[left] > 0 else 0
  
  center = (left+right) // 2
  max_left  = Devided_Conquer(nums, left, center)
  max_right = Devided_Conquer(nums, center+1, right)
  
  left_Sum = 0
  maxLeft_Sum = nums[center]

  for i in range(center-1, left-1, -1):
    left_Sum += nums[i]
    if left_Sum > maxLeft_Sum:
      maxLeft_Sum = left_Sum
  
  right_sum = 0
  max_right_sum = nums[center+1]

  for i in range(center+2, right+1):
    right_sum += nums[i]
    if right_sum > max_right_sum:
      max_right_sum = right_sum
  print("max_left:{0}, max_right:{1} ".format(maxLeft_Sum,max_right_sum))
  print("left:{0}, right:{1}, mid:{2}".format(max_left, max_right, maxLeft_Sum+max_right_sum))
  return max(max_left, max_right, maxLeft_Sum+max_right_sum)

def One_Pass(nums):
  max_sum = nums[0]
  this_sum = nums[0]
  for num in nums[1:]:
    this_sum = max(num, this_sum+num)
    if this_sum > max_sum:
      max_sum = this_sum
  return max_sum

if __name__ == '__main__':
  nums = [-2, 1,-3, 4,-1, 2, 1, -5, 4]
  print(One_Pass(nums))