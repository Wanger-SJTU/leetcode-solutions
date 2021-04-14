/*
 * @lc app=leetcode.cn id=208 lang=cpp
 *
 * [208] 实现 Trie (前缀树)
 */

#include "leetcode.h"

// @lc code=start
class Trie
{
public:
  /** Initialize your data structure here. */
  Trie() : children(26) {}

  /** Inserts a word into the trie. */
  void insert(string word)
  {
    Trie* node = this;
    for (char ch : word) {
      ch -= 'a';
      if (node->children[ch] == nullptr) {
        node->children[ch] = new Trie();
      }
      node = node->children[ch];
    }
    node->isWord = true;
  }

  /** Returns if the word is in the trie. */
  bool search(string word)
  {
    Trie* node = this->searchPrefix(word);
    return node != nullptr && node->isWord;
  }

  /** Returns if there is any word in the trie that starts with the given prefix. */
  bool startsWith(string prefix) { return this->searchPrefix(prefix) != nullptr; }

private:
  Trie* searchPrefix(string prefix)
  {
    Trie* node = this;
    for (char ch : prefix) {
      ch -= 'a';
      if (node->children[ch] == nullptr) {
        return nullptr;
      }
      node = node->children[ch];
    }
    return node;
  }

  vector<Trie*> children;
  bool isWord{false};
};

/**
 * Your Trie object will be instantiated and called as such:
 * Trie* obj = new Trie();
 * obj->insert(word);
 * bool param_2 = obj->search(word);
 * bool param_3 = obj->startsWith(prefix);
 */
// @lc code=end

int main() {}
