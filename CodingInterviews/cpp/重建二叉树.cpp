/**
 * Definition for binary tree
 * struct TreeNode {
 *     int val;
 *     TreeNode *left;
 *     TreeNode *right;
 *     TreeNode(int x) : val(x), left(NULL), right(NULL) {}
 * };
 */
class Solution {
public:
    TreeNode* reConstructBinaryTree(vector<int> pre,vector<int> vin) {
        return R(pre,0,pre.size(),vin,0,vin.size());
    }
    TreeNode* R(vector<int> a,int abegin,int aend, vector<int> b,int bbegin,int bend)
    {
        if(abegin >= aend || bbegin>=bend)
            return NULL;
        TreeNode* root = new TreeNode(a[abegin]);
        //root->val=a[abegin];
        int pivot;
        for(pivot=bbegin;pivot<bend;pivot++)
            if(b[pivot]==a[abegin])
                break;
        root->left=R(a,abegin+1,abegin+pivot-bbegin+1, b, bbegin,pivot);
        root->right=R(a,abegin+pivot-bbegin+1,aend,b,pivot+1,bend);
        return root;
    }
  
};