

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


if __name__ == '__main__':
	print(reverse(-101))