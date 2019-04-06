

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


def findMedianSortedArrays(self, nums1: List[int],nums2: List[int]) -> float:
  a, b = sorted((nums1, nums2), key=len)
  # a 短数组 b 长数组
  m, n = len(a), len(b)
  after = (m + n - 1) // 2
  lo, hi = 0, m
  while lo < hi:
    i = (lo + hi) // 2
    # b[0:after-i] 长数组 left
    if after-i-1 < 0 or a[i] >= b[after-i-1]:
      hi = i
    else:
      lo = i + 1
  i = lo
  nextfew = sorted(a[i:i+2] + b[after-i:after-i+2])##??
  return (nextfew[0] + nextfew[1 - (m+n)%2]) / 2.0


if __name__ == '__main__':
  nums1 = [1, 3]
  nums2 = [2, 4]
  print(get_median(nums1, nums2))