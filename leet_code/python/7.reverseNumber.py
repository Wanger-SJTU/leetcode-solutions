

# Given a 32-bit signed integer, reverse digits of an integer.

# Example 1:

# Input: 123
# Output:  321
# Example 2:

# Input: -123
# Output: -321
# Example 3:

# Input: 120
# Output: 21
import math

def cmp(a,b):
	return (a>b)-(a<b)

def reverse(x):
    """
    :type x: int
    :rtype: int
    """
    n = cmp(x, 0) * int(str(abs(x))[::-1])
    return n if n.bit_length() < 32 else 0

def reverse_math(n):
    if n.bit_length() >= 32: return 0
    sign = n >= 0
    res, n = 0, abs(n)
    while n:
        n, tmp = divmod(n,10)
        res = res*10+tmp
    return res

if __name__ == '__main__':
	print(reverse_math(10121))
