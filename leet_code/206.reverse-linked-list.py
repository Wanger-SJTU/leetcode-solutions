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
        pre = None
        cur = head 
        while cur != None:
            cur.next, pre, cur =  pre, cur,cur.next
        return pre

    def recursion(self, head):
        if head == None or head.next == None:
            return head
        node = self.reverseList(head.next)
        head.next.next = head
        head.next = None
        return node


