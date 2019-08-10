class Solution:
    def findNthDigit(self, n: int) -> int:
        start, size, step = 1, 1, 9
        while n > size * step:
            n, size, step, start = n - (size * step), size + 1, step * 10, start * 10
        return int(str(start + (n - 1) // size)[(n - 1) % size])

class Solution:
    def findNthDigit(self, n: int) -> int:
        #1-9:9 = 1*9*10^0
        #10-99:180 = 2*9*10
        #100-999:2700 = 3*9*10^2
        #1000-9999:36000 = 4*9*10^3
        n -= 1
        for digit in range(1, 11):
            first = 10**(digit - 1)
            if n < 9 * digit * first:
                return int(str(first + n // digit)[n % digit])
            n -= 9 * digit * first
            