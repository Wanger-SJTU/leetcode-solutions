/*
 * @lc app=leetcode.cn id=707 lang=cpp
 *
 * [707] 设计链表
 */
#include "leetcode.h"
// @lc code=start
class MyLinkedList
{
private:
  int val;
  MyLinkedList *next;

public:
  /** Initialize your data structure here. */
  MyLinkedList()
  {
    this->next = nullptr;
    this->val = 0;
  }
  MyLinkedList(int val)
  {
    this->next = nullptr;
    this->val = val;
  }
  MyLinkedList(int val, MyLinkedList *node)
  {
    this->next = node;
    this->val = val;
  }
  /** Get the value of the index-th node in the linked list. If the index is
   * invalid, return -1. */
  int get(int index)
  {
    MyLinkedList *pNode = this->next;
    for (int i = 0; i < index; i++) {
      if (pNode->next != nullptr) {
        pNode = pNode->next;
        cout << pNode->val << endl;
      } else {
        return -1;
      }
    }
    return pNode->val;
  }

  /** Add a node of value val before the first element of the linked list. After
   * the insertion, the new node will be the first node of the linked list. */
  void addAtHead(int val)
  {
    MyLinkedList *phead = this->next;
    MyLinkedList *newHead = new MyLinkedList(val);
    this->next = newHead;
    newHead->next = phead;
  }

  /** Append a node of value val to the last element of the linked list. */
  void addAtTail(int val)
  {
    MyLinkedList *pNode = this;
    while (pNode->next != nullptr) {
      pNode = pNode->next;
    }
    pNode->next = new MyLinkedList(val);
  }

  /** Add a node of value val before the index-th node in the linked list. If
   * index equals to the length of linked list, the node will be appended to the
   * end of linked list. If index is greater than the length, the node will not
   * be inserted. */
  void addAtIndex(int index, int val)
  {
    MyLinkedList *pNode = this;
    for (int i = 0; i < index; i++) {
      if (pNode->next != nullptr) {
        pNode = pNode->next;
      } else {
        return;
      }
    }
    pNode->next = new MyLinkedList(val, pNode->next);
  }

  /** Delete the index-th node in the linked list, if the index is valid. */
  void deleteAtIndex(int index)
  {
    MyLinkedList *pNode = this;
    for (int i = 0; i < index; i++) {
      if (pNode->next != nullptr) {
        pNode = pNode->next;
      } else {
        return;
      }
    }
    if (pNode->next != nullptr) pNode->next = pNode->next->next;
  }
  ~MyLinkedList()
  {
    delete next;
    next = nullptr;
    val = 0;
  }
};

/**
 * Your MyLinkedList object will be instantiated and called as such:
 * MyLinkedList* obj = new MyLinkedList();
 * int param_1 = obj->get(index);
 * obj->addAtHead(val);
 * obj->addAtTail(val);
 * obj->addAtIndex(index,val);
 * obj->deleteAtIndex(index);
 */
// @lc code=end
