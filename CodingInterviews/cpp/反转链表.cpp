/*
struct ListNode {
	int val;
	struct ListNode *next;
	ListNode(int x) :
			val(x), next(NULL) {
	}
};*/
#define null NULL
class Solution 
{
public:
    ListNode* ReverseList(ListNode* pHead) 
    {
        ListNode* reversedHead=NULL;
        ListNode* current=pHead;
        ListNode* tmp=NULL;
        ListNode* pre=null;
         
        while(current!=null)
        {
             tmp=current->next;
             current->next=pre;
             if(tmp==null)
                 reversedHead=current;
             pre=current;
             current=tmp;
  
         }
     return reversedHead;
    }
};