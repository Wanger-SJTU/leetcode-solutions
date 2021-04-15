/**
 * Definition for singly-linked list.
 * struct ListNode {
 *     int val;
 *     ListNode *next;
 *     ListNode(int x) : val(x), next(NULL) {}
 * };
 */
class Solution {
public:
    bool isPalindrome(ListNode* head) {
         ListNode* q = head; //快指针
        ListNode* cur = head, * pre = NULL; //反转链表的模板
        while(q && q->next) { 
            q = q->next->next; //2倍慢指针的速度
            ListNode* temp = cur->next; //反转链表的模板
            cur->next = pre;
            pre = cur;
            cur = temp;
        }
        if(q) cur = cur->next; //奇数链表处理
        while(pre) { //开始对比
            if(pre->val != cur->val) return false;
            pre = pre->next;
            cur = cur->next;
        }
        return true;
    }
};