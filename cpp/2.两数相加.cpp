/*
 * @lc app=leetcode.cn id=2 lang=cpp
 *
 * [2] 两数相加
 */
#include "leetcode.h"

//  * Definition for singly-linked list.
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
  ListNode *addTwoNumbers(ListNode *l1, ListNode *l2)
  {
    if (l1 == nullptr && l2 == nullptr) return nullptr;
    if (l1 == nullptr || l2 == nullptr) {
      return l1 == nullptr ? l2 : l1;
    }
    int tmp_res = l1->val + l2->val;
    ListNode *pNode = new ListNode(tmp_res % 10);
    pNode->next = addTwoNumbers(l1->next, l2->next);
    if (tmp_res >= 10) {
      pNode->next = addTwoNumbers(pNode->next, new ListNode(1));
    }
    return pNode;
  }
};
// @lc code=end
