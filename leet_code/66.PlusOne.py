
from typing import List
def plusOne(digits: List[int]) -> List[int]:

    flag = True
    for i in range(len(digits)-1, -1, -1):
        if flag:
            digits[i] = digits[i]+1
        if digits[i] > 9:
            digits[i] = digits[i]%10
            if i == 0:
                digits.insert(0, 1)
        else:
            return digits
    return digits
if __name__ == "__main__":
    print(plusOne([9]))