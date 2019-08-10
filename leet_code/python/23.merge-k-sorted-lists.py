#
# @lc app=leetcode id=23 lang=python3
#
# [23] Merge k Sorted Lists
#
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def mergeKLists(self, lists: List[ListNode]) -> ListNode:
        result=[]
        for i in range(len(lists)):
            while lists[i]:
                result.append(lists[i].val)
                lists[i]= lists[i].next
        result.sort()
        head, node = ListNode(0), ListNode(0)
        head = node
        for x in range(len(result)):
            node.next= ListNode(result[x])
            node = node.next
        final= head.next
        return final

