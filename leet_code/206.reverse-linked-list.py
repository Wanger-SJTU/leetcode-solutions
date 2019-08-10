#
# @lc app=leetcode id=206 lang=python3
#
# [206] Reverse Linked List
#
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def reverseList(self, head: ListNode) -> ListNode:
        def iterative(head):
            pre,cur = None, head
            while cur:
                nxt = cur.next
                cur.next = pre
                pre = cur
                cur = nxt
            return pre

        def recursively(head):
            if not head or not head.next:
                return head
            node = recursively(head.next)
            head.next.next = head
            head.next = None
            return node
        
        return iterative(head)



