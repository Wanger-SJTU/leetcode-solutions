class Solution:
    def isPerfectSquare(self, x: int) -> bool:
        low = 0
        high = x
        if x <= 1:
            return True
        while low <= high:
            mid =  (low + high) // 2
            if mid ** 2 == x:
                return True
            elif mid ** 2 < x:
                low = mid + 1
            else:
                high = mid - 1    
        return False