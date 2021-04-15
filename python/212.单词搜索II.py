class Trie:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.trie = {}
        

    def insert(self, word: str) -> None:
        """
        Inserts a word into the trie.
        """
        t = self.trie
        for i in word:
            if i not in t:
                t[i] = {}
            t = t[i]
        t['#'] = True
        

    def search(self, word: str) -> bool:
        """
        Returns if the word is in the trie.
        """
        t = self.trie
        for i in word:
            if i not in t:
                return False
            t = t[i]
        if '#' not in t:
            return False
        return True
        

    def startsWith(self, prefix: str) -> bool:
        """
        Returns if there is any word in the trie that starts with the given prefix.
        """
        t = self.trie
        for i in prefix:
            if i not in t:
                return False
            t = t[i]
        return True

class Solution:
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        trieNode = Trie()
        for word in words:
            trieNode.insert(word)
        res = []
        
        h,w = len(board), len(board[0])

        def dfs(i, j, path, node):
            if '#' in node.keys() and node['#']:
                res.append(path)
                node['#'] = False
            if i < 0 or i >= h or j < 0 or j >= w:
                return
            tmp = board[i][j]
            node = node.get(tmp, None)
            if not node:
                return
            board[i][j] = "*"
            dfs( i+1, j, path+tmp, node)
            dfs( i-1, j, path+tmp, node)
            dfs( i, j-1, path+tmp, node)
            dfs( i, j+1, path+tmp, node)
            board[i][j] = tmp
        
        for i in range(h):
            for j in range(w):
                dfs(i, j, "", trieNode.trie)
        return res