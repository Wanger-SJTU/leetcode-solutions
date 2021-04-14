/*
 * @lc app=leetcode.cn id=21 lang=cpp
 *
 * [21] 合并两个有序链表
 */
#include "common.h"

// Definition for singly-linked list.
struct ListNode {
  int val;
  ListNode* next;
  ListNode(int x) : val(x), next(NULL) {}
};
// @lc code=start
class Solution {
 public:
  ListNode* mergeTwoLists(ListNode* l1, ListNode* l2) {
    if (l1 == nullptr || l2 == nullptr) {
      return l1 == nullptr ? l2 : l1;
    }
    ListNode* dummpy = new ListNode(0);
    ListNode* pHead = dummpy;
    while (l1 != nullptr && l2 != nullptr) {
      if (l1->val >= l2->val) {
        pHead->next = new ListNode(l2->val);
        l2 = l2->next;
      } else {
        pHead->next = new ListNode(l1->val);
        l1 = l1->next;
      }
      pHead = pHead->next;
    }
    ListNode* tmp = l1 == nullptr ? l2 : l1;
    while (tmp != nullptr) {
      pHead->next = new ListNode(tmp->val);
      pHead = pHead->next;
      tmp = tmp->next;
    }
    return dummpy->next;
  }
};
// @lc code=end
