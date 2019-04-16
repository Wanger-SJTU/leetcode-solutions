class Solution {
public:
    bool IsBalanced_Solution(TreeNode* pRoot) 
    {
        if(pRoot == NULL)
            return true;
        if(!(IsBalanced_Solution(pRoot->left) || !IsBalanced_Solution(pRoot->right)))
            return false;
        return abs(GetDepth(pRoot->left)-GetDepth(pRoot->right)) <= 1;
    }
    int GetDepth(TreeNode* pRoot)
    {
        if(pRoot == NULL)
            return 0;
        auto left = GetDepth(pRoot->left);
        auto right = GetDepth(pRoot->right);
        return left>right ? left+1:right+1;
    }
};



/*
 *solutions 2
 *  
*/
class Solution {
public:
    bool IsBalanced_Solution(TreeNode* pRoot) 
    {
        int h = 0;
        return IsBalanced(pRoot, h);
    }
    bool IsBalanced(TreeNode* pRoot, int &height) 
    {
        if(!pRoot) return true;
        int left=0,right=0;
        if(!IsBalanced(pRoot->left,left)) return false;
        if(!IsBalanced(pRoot->right,right)) return false;
        if(abs(left-right) > 1) return false;
        height = max(left,right) + 1;
        return true;
    }
};