class TrieNode(object):

    def __init__(self):
        self._children = {}
        self.is_word = False


class MyTrie(object):    
    def __init__(self):
        self.root = TrieNode()

# 1. Each node is character
# 2. All subtrees/children under a node are words 
# with the prefix of the parent node
# 3. Terminating field to indicate a node is end of a word in the trie

a->[n, d, e]
a->[n, d, e]
ad