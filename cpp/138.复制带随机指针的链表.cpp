/*
// Definition for a Node.
class Node {
public:
    int val;
    Node* next;
    Node* random;
    
    Node(int _val) {
        val = _val;
        next = NULL;
        random = NULL;
    }
};
*/

class Solution {
public:
    Node* copyRandomList(Node* head) {
        if (head == nullptr) {
            return nullptr;
        }

    // Creating a new weaved list of original and copied nodes.
    Node* ptr = head;
    while (ptr != nullptr) {

      Node* newNode = new Node(ptr->val);

      newNode->next = ptr->next;
      ptr->next = newNode;
      ptr = newNode->next;
    }

    ptr = head;

    while (ptr != nullptr) {
      ptr->next->random = (ptr->random != nullptr) ? ptr->random->next : nullptr;
      ptr = ptr->next->next;
    }

    // Unweave the linked list to get back the original linked list and the cloned list.
    // i.e. A->A'->B->B'->C->C' would be broken to A->B->C and A'->B'->C'
    Node* ptr_old_list = head; // A->B->C
    Node* ptr_new_list = head->next; // A'->B'->C'
    Node* head_old = head->next;
    while (ptr_old_list != nullptr) {
      ptr_old_list->next = ptr_old_list->next->next;
      ptr_new_list->next = (ptr_new_list->next != nullptr) ? ptr_new_list->next->next : nullptr;
      ptr_old_list = ptr_old_list->next;
      ptr_new_list = ptr_new_list->next;
    }
    return head_old;
  }
};