
'''
base:
    N = 1, 1st player : lose 
    N = 2, 1st player : win

guess:
    N%2==0, 1st player : win
    N%2==1, 1st player : lose

for N = 2(k + 1), the player can win, 
since she can substract 1 from 2k + 2, 
making her opponent face the situation 2k + 1 to lose, 
meaning she will win.


'''


class Solution:
    def divisorGame(self, N: int) -> bool:
        return not N%2