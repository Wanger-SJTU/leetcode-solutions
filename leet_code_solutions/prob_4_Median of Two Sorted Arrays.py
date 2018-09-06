

def get_median(nums1, nums2):
  nums = []
  idx1 = 0
  idx2 = 0
  while idx1 <len(nums1) and idx2 < len(nums2):
    if nums1[idx1] < nums2[idx2]:
      nums.append(nums1[idx1])
      idx1 += 1
    else:
      nums.append(nums2[idx2])
      idx2 += 1
  while idx1 < len(nums1):
    nums.append(nums1[idx1])
    idx1 += 1
  while idx2 < len(nums2):
    nums.append(nums2[idx2])
    idx2 += 1
  print(nums)
  if len(nums) % 2 == 0:
    return (nums[len(nums)//2]+nums[len(nums)//2-1])/2
  else:
    return nums[len(nums)//2+1]

if __name__ == '__main__':
  nums1 = [1, 3]
  nums2 = [2, 4]
  print(get_median(nums1, nums2))