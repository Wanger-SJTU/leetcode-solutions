
class Solution:
    """
    @param a: the array a
    @param k: the integer k
    @param target: the integer target
    @return: return the number of legal schemes
    """
    def getAns(self, a, k, target):
        res = 0
        # write your code here
        def search(nums, k_idx, target):
            nonlocal res
            if target < 0:
                return
            if k_idx == 0 and target==0:
                res += 1
                return

            for i in range(len(nums)):
                if nums[i] <= target:
                    search(nums[i+1:], k_idx-1, target-nums[i])
        b,c = [],[]
        for item in a:
            if item&1:
                b.append(item)
            else:
                c.append(item)
        search(b, k, target)
        search(c, k, target)
        return res
