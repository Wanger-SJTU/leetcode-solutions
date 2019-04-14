/*
struct TreeNode {
	int val;
	struct TreeNode *left;
	struct TreeNode *right;
	TreeNode(int x) :
			val(x), left(NULL), right(NULL) {
	}
};*/
class Solution {
public:
    vector<int> PrintFromTopToBottom(TreeNode* root) 
    {
        TreeNode* p = root;
        queue<TreeNode*> node;
        vector<int> res;
        if(p==NULL) return res;
        node.push(p);
        while(!node.empty())
        {
            auto cur = node.front();
            res.push_back(cur->val);
            if(cur->left != NULL)
                node.push(cur->left);
            if(cur->right != NULL)
                node.push(cur->right);
            node.pop();
        }
        return res;
    }
};