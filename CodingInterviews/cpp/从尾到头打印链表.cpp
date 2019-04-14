/**
*  struct ListNode {
*        int val;
*        struct ListNode *next;
*        ListNode(int x) :
*              val(x), next(NULL) {
*        }
*  };
*/
class Solution {
public:
    vector<int> printListFromTailToHead(ListNode* head) {
        vector<int> result;
        for(auto iter = head; iter != NULL; iter=iter->next)
        {
            result.insert(result.begin(), iter->val);
        }
        return result;
    }
};