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
    ListNode* FindKthToTail(ListNode* pListHead, unsigned int k) {

        ListNode* p1 = pListHead;
        ListNode* p2 = pListHead;
        
        for(int i = 0;i<k;i++)
        {
            if(p1 == NULL)
                return NULL;
            else
                p1 = p1->next;
        }
        while(p1 != NULL)
        {
            p1 = p1->next;
            p2 = p2->next;
        }
        return p2;
    }
};