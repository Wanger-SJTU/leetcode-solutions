#include "leetcode.h"
/**
 * Definition for singly-linked list.
 * struct ListNode {
 *     int val;
 *     ListNode *next;
 *     ListNode() : val(0), next(nullptr) {}
 *     ListNode(int x) : val(x), next(nullptr) {}
 *     ListNode(int x, ListNode *next) : val(x), next(next) {}
 * };
 */
class Solution {
public:
    ListNode* deleteDuplicates(ListNode* head) {
        ListNode* dummpy = new ListNode();
        dummpy->next = head;
        ListNode* pre = dummpy;
        ListNode* cur = head;
        while (cur != nullptr && cur->next != nullptr) {
            if (cur->val == cur->next->val) {
                while(cur != nullptr && cur->next != nullptr && 
                     cur->val == cur->next->val) {
                         cur = cur->next;
                    }
                cur = cur->next;
                pre->next = cur;
            } else {
                cur = cur->next;
            pre = pre->next;
            }
            
        }
        return  dummpy->next;
    }
};