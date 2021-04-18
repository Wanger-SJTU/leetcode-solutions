#include "leetcode.h"
struct Node {
    int key, val;
    int freq;
    Node* pre;
    Node* next;
    Node(): key(0), val(0), pre(nullptr), next(nullptr) {}
    Node(int _key, int _val): key(_key), val(_val), pre(nullptr), next(nullptr) {
        freq = 1;
    }
};

class DList {
private:

    Node* head;
    Node* tail;


public:
    int size;
    DList() {
        size = 0;
        head = new Node;
        tail = new Node;
        head->next = tail;
        tail->pre = head;       
        
    }
    void addToHead(Node* node) {
        node->next = head->next;
        head->next->pre = node;
        node->pre = head;
        head->next = node;
        ++size;
    }
    
    Node* removeNode(Node* node) {
        node->pre->next = node->next;
        node->next->pre = node->pre;
        --size;
        return node;
    }
    
    Node* removeTail() {
        Node* to_remove = tail->pre;
        return removeNode(to_remove);
    }
};

class LFUCache {
private:
    int capacity;
    int size;
    int min_freq;
    unordered_map<int, Node*> cache;
    unordered_map<int, DList> freq_table;
public:
    LFUCache(int _capacity): capacity(_capacity) {
        size = 0;
        min_freq = 0;
    }
    
    int get(int key) {

        if (cache.count(key) != 0) {
            Node* temp = cache[key];
            freq_table[temp->freq].removeNode(temp);
            if (min_freq == temp->freq && freq_table[min_freq].size == 0) {
                ++min_freq;
            }
            ++temp->freq;
            freq_table[temp->freq].addToHead(temp);
            return temp->val;
        }else {
            return -1;
        }

    }
    
    void put(int key, int value) {
        if (capacity == 0) {
            return;
        }
        if (cache.count(key) != 0) {
            Node* temp = cache[key];
            freq_table[temp->freq].removeNode(temp);
            if (min_freq == temp->freq && freq_table[min_freq].size == 0) {
                ++min_freq;
            }
            ++temp->freq;
            temp->val = value;
            freq_table[temp->freq].addToHead(temp);
            return;
        }else if (size == capacity) {
            Node* to_remove = freq_table[min_freq].removeTail();
            cache.erase(to_remove->key);
            delete to_remove;
            --size;          
        }
        
        Node* cur = new Node(key, value);
        cache[key] = cur;
        min_freq = 1;
        freq_table[1].addToHead(cur);
        ++size;

    }
};