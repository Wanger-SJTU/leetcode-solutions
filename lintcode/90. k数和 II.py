class Solution:
    """
    @param: A: an integer array
    @param: k: a postive integer <= length(A)
    @param: targer: an integer
    @return: A list of lists of integer
    """
    def kSumII(self, A, k, target):
        # write your code here
        res = []
        def search(nums, path, k_idx, target):
            if target < 0:
                return
            if k_idx == 0 and target==0:
                    res.append(sorted(path))
                    return

            for i in range(len(nums)):
                if nums[i] < target:
                    search(nums[i+1:], path+[nums[i]], k_idx-1, target-nums[i])
        search(A, [], k, target)

        return res
