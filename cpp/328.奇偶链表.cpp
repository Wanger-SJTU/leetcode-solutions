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
    ListNode* oddEvenList(ListNode* head) {
         if (head == NULL )
            return head;
        ListNode *_swap = head->next; //要交换的节点的 前屈
        ListNode *p = head;             //把奇结点用尾插法插入到p->next
        while (_swap != NULL && _swap->next != NULL) {
            //每一次循环，要交换一个结点，并且后移一位，所以需要检查两个结点
            ListNode *Tmp = _swap->next;  //保留交换结点，用于插入
            _swap = _swap->next = _swap->next->next; 
        //先进行删除 _swap后面的结点， 然后 让_swap 后移一位
            Tmp->next = p->next;  //把奇结点  尾插法 插入到p->next上
            p = p->next = Tmp;    //p要记得一直指向  奇结点的尾端
        }
        return head;
    }
};