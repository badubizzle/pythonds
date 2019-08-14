class TrieNode(object):

    def __init__(self, character=None):
        self._children = {}
        self.is_word = False
        self.character = character


class MyTrie(object):
    def __init__(self):
        self.root = TrieNode()

    def insert(self, word):

        parent_node = self.root

        for character in word:
            if character not in parent_node._children:
                parent_node._children[character] = TrieNode(character)
            parent_node = parent_node._children[character]

        parent_node.is_word = True

    def print_trie(self):
        if self.root is None:
            return []

        visited = []
        stack = [self.root]

        while len(stack) > 0:
            node = stack.pop()

            if node not in visited:
                visited.append(node.character)
                # import pdb
                # pdb.set_trace()

            if node._children:
                for child in node._children:
                    stack.append(node._children[child])

        return visited

    def find_word(self, word):
        parent_node = self.root

        for character in word:
            # import pdb
            # pdb.set_trace()

            if character not in parent_node._children:
                return False

            parent_node = parent_node._children[character]

        return parent_node.is_word


# trie = * ->{}
# for each character in "andela":
# #insert character at next node
# first loop -> character = a
# parent node = root
# check if charater in parent's children
# is 'a' in {}? No
# insert 'a' node in parent
# * -> {'a' -> {} }
# parent = a
# check if n is in parent's children
# is 'n' in {} ? No
# insert 'n' node in parent
# * -> {'a' -> {'n'->{}}}
# parent = n
# check if d is in parent's children
# is 'd' in {}? No
# insert 'd' node in parent
# * -> {'a': {'n': {'d': {is_word: true}}}}
# 1. Each node is character
# 2. All subtrees/children under a node are words
# with the prefix of the parent node
# 3. Terminating field to indicate a node is end of a word in the trie
# a -> [n, d, e]
# a -> [n, d, e]
# ad

# * -> {'h' -> {} }
# * -> {'h' -> {'e' -> {}} }
# * -> {'h' -> {'e' -> {'l' -> {}}} }
# * -> {'h' -> {'e' -> {'l' -> {'l' -> {}}}} }
# * -> {'h' -> {'e' -> {'l' -> {'l' -> {'o' -> {*isword*}}}}} }
# * -> {'h' -> {'e' -> {'l' -> {'l' -> {'o' -> {*isword*}}}}} }
# * -> {'h' -> {'i' -> {*isword*}, 'e' -> {'l' -> {'l' -> {'o' -> {*isword*}}}}} }
# * -> {'e' -> {}, 'h' -> {'i' -> {*isword*}, 'e' -> {'l' -> {'l' -> {'o' -> {*isword*}}}}} }
# * -> {'e' -> {'g' -> {}}, 'h' -> {'i' -> {*isword*}, 'e' -> {'l' -> {'l' -> {'o' -> {*isword*}}}}} }
# * -> {'e' -> {'g' -> {'g' -> {*isword*}}}, 'h' -> {'i' -> {*isword*}, 'e' -> {'l' -> {'l' -> {'o' -> {*isword*}}}}} }


trie = MyTrie()

trie.insert('hello')
trie.insert('hi')
trie.insert('egg')
trie.insert('eg')
trie.insert('long')
trie.insert('him')
# print(trie.find_word('gun'))
print(trie.find_word('eig'))
print(trie.print_trie())
