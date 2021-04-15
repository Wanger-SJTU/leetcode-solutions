#
# @lc app=leetcode.cn id=381 lang=python3
#
# [381] O(1) 时间插入、删除和获取随机元素 - 允许重复
#
import random

class RandomizedCollection:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.l, self.d = [], collections.defaultdict(set)


    def insert(self, val: int) -> bool:
        """
        Inserts a value to the collection. Returns true if the collection did not already contain the specified element.
        """
        self.d[val].add(len(self.l))
        self.l.append(val)
        return len(self.d[val])==1

    def remove(self, val: int) -> bool:
        """
        Removes a value from the collection. Returns true if the collection contained the specified element.
        """
        if val not in self.d:
            return False
        i, newVal = self.d[val].pop(), self.l[-1]
        len(self.d[val]) > 0 or self.d.pop(val, None)
        if newVal in self.d:
            self.d[newVal] = (self.d[newVal] | {i}) - {len(self.l)-1}
        self.l[i] = newVal
        self.l.pop()
        return True


    def getRandom(self) -> int:
        """
        Get a random element from the collection.
        """
        return random.choice(self.l)



# Your RandomizedCollection object will be instantiated and called as such:
# obj = RandomizedCollection()
# param_1 = obj.insert(val)
# param_2 = obj.remove(val)
# param_3 = obj.getRandom()

