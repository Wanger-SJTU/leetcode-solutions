#include "leetcode.h"
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
/**
 * Definition for a binary tree node.
 * struct TreeNode {
 *     int val;
 *     TreeNode *left;
 *     TreeNode *right;
 *     TreeNode() : val(0), left(nullptr), right(nullptr) {}
 *     TreeNode(int x) : val(x), left(nullptr), right(nullptr) {}
 *     TreeNode(int x, TreeNode *left, TreeNode *right) : val(x), left(left), right(right) {}
 * };
 */

class Solution {
public:
	TreeNode* sortedListToBST(ListNode* head) {
		if (head == nullptr) {
			return nullptr;
		}
		int len = 0;
		pHead = head;
		while (head != nullptr) {
			len++;
			head = head->next;
		}
		return BuildBST(0, len - 1);
	}
private:
	TreeNode* BuildBST(int left, int right) {
		if (left > right) {
            return nullptr;
        }
        int mid = (left + right + 1) / 2;
        TreeNode* root = new TreeNode();
        root->left = BuildBST(left, mid - 1);
        root->val = pHead->val;
        pHead = pHead->next;
        root->right = BuildBST(mid + 1, right);
        return root;
	}
private:
	ListNode* pHead;
};
