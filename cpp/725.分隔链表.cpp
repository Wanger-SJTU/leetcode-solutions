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
    vector<ListNode*> splitListToParts(ListNode* root, int k) {
        //（1）先数有多少块小糖，得n块；——> 计算链表长度length
        ListNode *p = root;
        int length = 0;
        while(p){
            length++;
            p = p->next;
        }

        //（2）将n块小糖分给k个小朋友：从左往右均分(n/k)块；——> 向量vector直接初始化为k个均分值（length/k）
        vector<int> splitLength(k,length/k);

        //（3）将剩下的(n%k)块小糖再从左往右1人1块，直至分完。——> 向量vector从0到length%k增加1
        for(int i = 0; i < length % k; i++)
            splitLength[i] += 1;

        //分割链表
        vector<ListNode*> splitList;

        //虚拟头结点：dummyHead大法好
        ListNode dummyHead(0);
        dummyHead.next = root;
        auto pre = root;

        int i = 0;//记录splitLength中序号，已取出索引值
        int num = 0;//记录子链表的长度
        while(root){
            num++;
            pre = root;
            root = root->next;

            if(num == splitLength[i]){
                i++;//准备记录下一个splitLength中的序号
                num = 0;//恢复子链表长度初始值，准备记录下一个子链表
                pre->next = NULL;
                splitList.push_back(dummyHead.next);//将子链表压入栈中
                pre = root;
                dummyHead.next = root;
            }
        }

        //糖果小于小朋友人数，每个人分零块
        while(i++ < k)
            //将root(上面遍历一遍为空，无需再申请空node)直接压入栈中，然后i值加1，简单干练粗暴
            splitList.push_back(root);

        return splitList;
    }
};