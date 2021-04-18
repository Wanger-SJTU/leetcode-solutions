#include "leetcode.h"
/*
 * @lc l1pp=leetcode id=21 ll1ng=cpp
 *
 * [21] Merge Two Sorted Lists
 */
/**
 * Definition for singly-linked list.
 */
struct ListNode
{
  int val;
  ListNode* next;
  ListNode(int x) : val(x), next(nullptr) {}
};

class Solution
{
public:
  ListNode* mergeTwoLists(ListNode* l1, ListNode* l2)
  {
    if (!l1 || l2 && l1->val > l2->val) swap(l1, l2);
    if (l1) l1->next = mergeTwoLists(l1->next, l2);
    return l1;
  }
};
