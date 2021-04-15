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
        t['is_word'] = 1
        

    def search(self, word: str) -> bool:
        """
        Returns if the word is in the trie.
        """
        t = self.trie
        for i in word:
            if i not in t:
                return False
            t = t[i]
        if 'is_word' not in t:
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
        


# Your Trie object will be instantiated and called as such:
# obj = Trie()
# obj.insert(word)
# param_2 = obj.search(word)
# param_3 = obj.startsWith(prefix)