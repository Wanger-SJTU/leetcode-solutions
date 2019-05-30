#
# @lc app=leetcode id=208 lang=python3
#
# [208] Implement Trie (Prefix Tree)
#
# https://leetcode.com/problems/implement-trie-prefix-tree/description/
#
# algorithms
# Medium (38.30%)
# Likes:    1561
# Dislikes: 31
# Total Accepted:    177.9K
# Total Submissions: 463.5K
# Testcase Example:  '["Trie","insert","search","search","startsWith","insert","search"]\n[[],["apple"],["apple"],["app"],["app"],["app"],["app"]]'
#
# Implement a trie with insert, search, and startsWith methods.
# 
# Example:
# 
# 
# Trie trie = new Trie();
# 
# trie.insert("apple");
# trie.search("apple");   // returns true
# trie.search("app");     // returns false
# trie.startsWith("app"); // returns true
# trie.insert("app");   
# trie.search("app");     // returns true
# 
# 
# Note:
# 
# 
# You may assume that all inputs are consist of lowercase letters a-z.
# All inputs are guaranteed to be non-empty strings.

class TreeNode:
    def __init__(self):
        self.isWord = False
        self.children = [None]*26

class Trie:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.root = TreeNode()

    def insert(self, word: str) -> None:
        """
        Inserts a word into the trie.
        """
        pRoot = self.root
        for char in word:
            if not pRoot.children[ord(char)-ord('a')]:
                pRoot.children[ord(char)-ord('a')] = TreeNode()
            pRoot = pRoot.children[ord(char)-ord('a')]
        pRoot.isWord = True

    def search(self, word: str) -> bool:
        """
        Returns if the word is in the trie.
        """
        pRoot = self.root
        for char in word:
            if not pRoot.children[ord(char)-ord('a')]:
                return False
            pRoot = pRoot.children[ord(char)-ord('a')]
        return pRoot.isWord
        

    def startsWith(self, prefix: str) -> bool:
        """
        Returns if there is any word in the trie that starts with the given prefix.
        """
        pRoot = self.root
        for char in prefix:
            if not pRoot.children[ord(char)-ord('a')]:
                return False
            pRoot = pRoot.children[ord(char)-ord('a')]
        return True 


# Your Trie object will be instantiated and called as such:
# obj = Trie()
# obj.insert(word)
# param_2 = obj.search(word)
# param_3 = obj.startsWith(prefix)

