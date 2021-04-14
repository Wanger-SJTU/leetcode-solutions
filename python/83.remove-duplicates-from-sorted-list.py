#
# @lc app=leetcode id=83 lang=python3
#
# [83] Remove Duplicates from Sorted List
#
# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def deleteDuplicates(self, head: ListNode) -> ListNode:
        if not head or not head.next: return head
        p1,p2 = head, head.next
        
        while p2:
            if p2.val == p1.val:
                p2=p2.next
                p1.next = p2
            else:
                p1.next = p2
                p1 = p2
                p2 = p1.next
        
        return head
# if __name__ == "__main__":
#     a = ListNode(1)
#     a.next = ListNode(1)
#     #a.next.next = ListNode(2)
#     s = Solution()
#     b = s.deleteDuplicates(a)
#     while b:
#         print(b.val)
#         b = b.next
