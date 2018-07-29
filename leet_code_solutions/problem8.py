
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
        number = ''
        converts = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9', '-', '+']
        pdb.set_trace()
        for character in string:
            if len(number) == 0 or character in converts[0:10]:
                if character == ' ':
                    continue
                if character in converts:
                    number = number + character
                elif character == '.':
                    break
                elif len(number) == 0:
                    return 0
                elif len(number) > 0:
                    break
            else:
                if character not in converts[0:10]:
                    break
        if len(number) == 0:
            return 0
        sign = 1
        result = 0
        start = 0
        for character in number:
            if character in converts[0:10]:
                break
            elif character == '-':
                sign = sign*-1
                start = start+1
            elif character == '+':
                start = start+1
        if start > 1:
            return 0
        for i in range(start,len(number)):
            if self.convert2num(number[i]) == -1:
                return 0
            result = result*10 + self.convert2num(number[i]) 
        result = sign*result
        if result < -2**31:
            result = -2**31
        if result > 2**31 -1:
            return 2**31 -1
        return result

    def convert2num(self, string):
        dict_num = {'1':1, '2':2, '3':3, '4':4, '5':5, '6':6, '7':7, '8':8, '9':9, '0':0,  '-':-1, '+':-1}
        return dict_num[string]

if __name__ == '__main__':
    inputs = "4193 with words"
    '''
    input                               output
    '+- 1'                                0
    '4193 with words'                     4193
    '0-2'                                 0
    '   42'


    '''
    solution = Solution()
    print(solution.myAtoi(inputs))