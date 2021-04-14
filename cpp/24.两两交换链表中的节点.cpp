/*
 * @lc app=leetcode.cn id=24 lang=cpp
 *
 * [24] 两两交换链表中的节点
 */
#include "leetcode.h"

// Definition for singly-linked list.
struct ListNode
{
  int val;
  ListNode *next;
  ListNode(int x) : val(x), next(NULL) {}
};
// @lc code=start
class Solution
{
public:
  ListNode *swapPairs(ListNode *head)
  {
    ListNode **pp = &head, *a, *b;
    while ((a = *pp) && (b = a->next)) {
      a->next = b->next;
      b->next = a;
      *pp = b;
      pp = &(a->next);
    }
    return head;
  }
};
// @lc code=end
