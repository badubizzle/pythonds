class TrieNode(object):

    def __init__(self, character=None):
        self._children = {}
        self.is_word = False
        self.word = None
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
        parent_node.word = word

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

    def get_all_words_naive(self):

        stack = [self.root]
        result = []
        while len(stack) > 0:
            node = stack.pop()
            if node.is_word:
                result.append(node.word)

            for letter, n in node._children.items():
                stack.append(n)

        return result

    def get_all_words(self):
        return self.get_all_words_from_node(self.root)

    def get_all_words_from_node(self, node):

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

        result = []

        # iteration 1
        # letter = h
        # [ 'h', 'e ]
        # 'h' -> {'i' -> {*isword*}, 'e' -> {'l' -> {'l' -> {'o' -> {*isword*}}}}

        # ['hi']
        # ['hello']
        #  iteration 2
        # letter = i
        # ['i']

        # iteration 3
        # letter = e
        # result = ['ello']

        # iteration 4
        # letter = l
        # result = ['llo]

        # iteration 5
        # letter = l
        # result['lo']

        # iteration 6
        # letter o
        # result ['o]

        for letter, n in node._children.items():

            if not n.is_word:
                for suffix in self.get_all_words_from_node(n):
                    result.append(letter + suffix)
            else:
                result.append(letter)

                if len(n._children) > 0:
                    for suffix in self.get_all_words_from_node(n):
                        result.append(letter + suffix)

                #'hi', 'him'
                # i.is_word = True
                # i.children is not empty

        return result

    def find_prefixes(self, prefix):

        # ['hi', 'him', 'hello', 'cool', 'eg', 'egg', 'long']
        # prefix ="him", prefix to him, his
        # node = "", find all words starting from that node

        # case 1:
        # Does the prefix exists in the trie
        # if the prefix doesnt exist return empty []

        # Case 2:
        # if prefix (node) exists
        # if prefix node is a word result.append(prefix)
        # check if prefix node has children
        # find all suffixes that are in the subtrie (or children) of the prefix node
        # for each suffix, ressult.append(prefix+suffix)
        find_word = self.find_word(prefix)

        result = []

        if not find_word:
            return []

        if find_word.is_word:
            result.append(prefix)

        if len(find_word._children) > 0:
            for suffix in self.get_all_words_from_node(find_word):
                result.append(prefix + suffix)

        return result

    def find_prefix_naive(self, prefix):
        stack = [self.root]
        result = []
        while len(stack) > 0:
            node = stack.pop()
            if node.is_word and node.word.startswith(prefix):
                result.append(node.word)

            for letter, n in node._children.items():
                stack.append(n)

        return result

    def find_word(self, word):
        parent_node = self.root

        for character in word:
            # import pdb
            # pdb.set_trace()

            if character not in parent_node._children:
                return None

            parent_node = parent_node._children[character]

        return parent_node


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

#     *
#   /   \
# / \  / \


trie = MyTrie()

trie.insert('hello')
trie.insert('hi')
trie.insert('his')
trie.insert('egg')
trie.insert('eg')
trie.insert('long')
trie.insert('him')
trie.insert("cool")
# print(trie.find_word('eig'))
# print(trie.print_trie())

# print(trie.get_all_words())
# print(trie.get_all_words_naive())

print(trie.find_prefixes("hi"))
