#
# @lc app=leetcode id=203 lang=python
#
# [203] Remove Linked List Elements
#
# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution(object):
    def removeElements(self, head, val):
        """
        :type head: ListNode
        :type val: int
        :rtype: ListNode
        """
        if not head:
            return None

        while head and head.val == val:
            head = head.next
        p = head
        while p:
            if p.next and p.next.val == val:
                p.next = p.next.next
            else:
                p = p.next
        return head
                
if __name__ == "__main__":
    s = Solution()
    a = [1,2,6,3,4,5,6]
    head = ListNode(0)
    p = head
    for i in a:
        p.next = ListNode(i)
        p = p.next
    res = s.removeElements(head.next, 6)
    while res:
        print(res.val)
        res = res.next
