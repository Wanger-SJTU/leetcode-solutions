
import collections

def majorityElement_hashmap(nums):
    counts = collections.Counter(nums)
    return max(counts.keys(), key=counts.get)

# num of majorityElement > n//2
def  majorityElement_Sorting(nums):
    return sorted(nums)[len(nums)//2]

def Randomization(nums):
    majority_count = len(nums)//2
    while True:
        candidate = random.choice(nums)
        if sum(1 for elem in nums if elem == candidate) > majority_count:
            return candidate