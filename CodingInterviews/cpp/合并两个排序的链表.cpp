/*
struct ListNode {
	int val;
	struct ListNode *next;
	ListNode(int x) :
			val(x), next(NULL) {
	}
};*/
class Solution {
public:
    ListNode* Merge(ListNode* pHead1, ListNode* pHead2)
    {
        ListNode *p1,*p2,*pre1,*p3;
        pre1 = p1 = pHead1; p2 = pHead2;
        while(p1 && p2)
        {
            if(p1->val > p2->val)
            {
                pre1->next = p2;
                p3 = p2->next;
                p2->next = p1;
                p2 = p3;
            }
            pre1 = p1;
            p1 = p1->next;
        }
        if(p2)
            pre1->next = p2;
         
        return pHead1;
    }
};