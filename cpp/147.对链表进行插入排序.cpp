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
    ListNode* insertionSortList(ListNode* head) {
        if (!head || !head->next)
                return head;
            ListNode *dummyhead = new ListNode(-1);//伪头指针
            dummyhead->next = head;
            ListNode *prev = head;
            ListNode *node = head->next;
            while (node)
            {
                if (node->val < prev->val)
                {
                    ListNode* temp = dummyhead;//！！temp要等于dummyhead，这样才可以比较第一个元素
                    while (temp->next->val < node->val)//！！！这里是temp->next：因为要修改前面的temp的指向
                    {
                        temp = temp->next;//指针后移
                    }
                    prev->next = node->next;
                    node->next = temp->next;
                    temp->next = node;
                    node = prev->next;//此时不用改变prev指向！因为prev没有变，只是待排序元素变了位置。
                }
                else
                {
                    prev = prev->next;
                    node = node->next;
                }
            }
            return dummyhead->next;//!!!不能返回head！！因为后面会改变head所指向内存的位置！
    }
};