#
# @lc app=leetcode id=24 lang=python3
#
# [24] Swap Nodes in Pairs
#
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def swapPairs(self, head: ListNode) -> ListNode:
        nhead = ListNode(0)
        pre, pre.next = nhead, head
        while pre.next and pre.next.next:
            a = pre.next
            b = a.next
            pre.next, b.next, a.next = b, a, b.next
            pre = a
        return nhead.next

# if __name__ == "__main__":
#     head = ListNode(1)
#     head.next = ListNode(2)
#     head.next.next = ListNode(3)
#     # head.next.next.next = ListNode(4)
#     s= Solution()
#     a = s.swapPairs(head)
#     while a:
#         print(a.val, end =' ')
#         a= a.next

