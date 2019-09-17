class Solution:
    """
    @param nums: an array containing n + 1 integers which is between 1 and n
    @return: the duplicate one
    """
    def findDuplicate(self, nums):
        # write your code here
        left,right = 1, len(nums)
        while left <= right:
            mid = left + (right-left)//2
            cnt = self.countNums(nums, left, mid)
            if left == right:
                if cnt > 1:
                    return left
                else:
                    break
            if cnt > mid-left+1:
                right = mid
            else:
                left = mid+1
        return -1

    def countNums(self, nums, srt, end):
        return sum([srt<=item <= end for item in nums])

