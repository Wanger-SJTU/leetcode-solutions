#
# @lc app=leetcode id=21 lang=python3
#
# [21] Merge Two Sorted Lists
#
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def mergeTwoLists(self, l1: ListNode, l2: ListNode) -> ListNode:
        newList  = ListNode(0)
        p = newList
        p1,p2 = l1, l2
        while p1 and p2:
            if p1.val < p2.val:
                p.next = ListNode(p1.val)
                p1 = p1.next
            else:
                p.next = ListNode(p2.val)
                p2 = p2.next
            p = p.next
        p.next = p1 if p1 else p2
        return newList.next
              
# if __name__ == "__main__":
#     a =  ListNode(1)
#     a.next = ListNode(2)
#     a.next.next = ListNode(4)
#     b =  ListNode(1)
#     b.next = ListNode(3)
#     b.next.next = ListNode(4)

#     s= Solution()
#     res = s.mergeTwoLists(a,b)
#     while res:
#         print(res.val,end='->')
#         res = res.next
