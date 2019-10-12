
'''
Implement atoi which converts a string to an integer.

The function first discards as many whitespace characters as necessary until the first non-whitespace character is found.
Then, starting from this character, takes an optional initial plus or minus sign followed by as many numerical digits as possible,
and interprets them as a numerical value.

The string can contain additional characters after those that form the integral number,
which are ignored and have no effect on the behavior of this function.

If the first sequence of non-whitespace characters in str is not a valid integral number,
or if no such sequence exists because either str is empty or it contains only whitespace characters,
no conversion is performed.

If no valid conversion could be performed, a zero value is returned.

'''
import pdb
class Solution(object):
    def myAtoi(self, string):
        """
        :type str: str
        :rtype: int
        """
        number,sign,point = '',1, False
        string = string.lstrip()
        for char in string:
            if char == '+':
                if len(number)==0:
                    continue
                else:
                    return 0
            elif  char == '-':
                if len(number)==0:
                    continue
                else:
                    sign *= -1
            elif char == '.':
                if point:
                    return 0
                point = True
                number += char
            elif char.isdigit():
                number += char
            else:
                return 0
        return sign*min(float(number), 2<<32-1) if point else sign*min(int(number), 2<<32-1)

if __name__ == '__main__':
    inputs = "4193"
    '''
    input                               output
    '+- 1'                                0
    '4193 with words'                     4193
    '0-2'                                 0
    '   42'


    '''
    solution = Solution()
    print(solution.myAtoi(inputs))
