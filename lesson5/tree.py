
# inoder(node=125):
import random
# inorder(left)
# do(node)
# inorder(161)

# 1 2 13 19 27 48 50 79 117 120 125 161
# current node = 1


class BNode():
    def __init__(self, value, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right

    def __repr__(self):
        result = {}
        result["node"] = self.value
        if self.left:
            result["left"] = self.left.value
        if self.right:
            result["right"] = self.right.value

        return str(result)

    def is_leaf(self):
        if self.right is None and self.left is None:
            return True
        else:
            return False

    def print_node(self):
        print(self.value)


class BTree():
    def __init__(self, root=None):
        self.root = root

    def bfs(self):
        queue = []
        visited = []
        if self.root:
            queue.append(self.root)

        while queue:
            current = queue.pop(0)
            if not current in visited:
                visited.append(current.value)
            if current.left:
                queue.append(current.left)
            if current.right:
                queue.append(current.right)

        return visited

    def preorder(self):
        self._preorder(self.root)

    def postorder(self):
        self._postorder(self.root)

    def inorder(self):
        self._inorder(self.root)

    def _preorder(self, node):
        if not node:
            return
        print(node.value)
        self._preorder(node.left)
        self._preorder(node.right)

    def _postorder(self, node):
        if not node:
            return
        self._postorder(node.left)
        self._postorder(node.right)
        print(node.value)

    def _inorder(self, node):
        if not node:
            return
        self._inorder(node.left)
        self._inorder(node.right)
        print(node.value)

    def dfs(self):
        if self.root is None:
            return []

        visited = []
        stack = [self.root]

        while len(stack) > 0:
            node = stack.pop()

            if node not in visited:
                visited.append(node)
                # node.visited = True
                # import pdb
                # pdb.set_trace()

            # if len(node.children)>0:
            #     for child in node.children:
            #         stack.append(child)

            if node.right:
                stack.append(node.right)
            if node.left:
                stack.append(node.left)
            # append right first, so left will be popped first
        return visited

        # [1]
        #  1  node = 7 []
        # /  \
        # 2   3 []
        # /\  /\
        # 4 5 6 7

        # visited [1, 2, 3, 4, 5, 6, 7]

    def insert(self, value):
        new_node = BNode(value)

        if self.root is None:
            self.root = new_node
        else:
            self._insert_with_node(self.root, value)

    # def find_node_with_value(self, value):
    #     return self._find_node_from(self.root, value)

    # # def delete_node(self, value):
    # #      if node is None:
    # #          return None

    # #     find_node = self.find_node_with_value(value)

    # #     if find_node[0].is_leaf() == True:

    # #         return 'this has no leaf'

    # def delete_with_value(self, value):
    #     # Case 1
    #     #  -> the node to be deleted is a leaf node
    #     #  => find the node, set the parent left or right to null
    #     self.delete_with_value_from_node(self.root, value)

    # def get_min(self, node):
    #     current_node = node
    #     while current_node is not None:
    #         current_node = current_node.left

    #     return current_node

    # def delete_with_value_from_node(self, node, value):

        # import pdb
        # pdb.set_trace()

        # if node.value == value:
        #     if node.is_leaf():
        #         #  3
        #         # / \
        #         # 2  4
        #         # delete 2
        #         # 2 = None
        #         #  3
        #         # / \
        #         # None 4
        #         node = None
        #         return None
        #     if node.left is not None and node.right is not None:
        #         #    20
        #         #  /    \
        #         # 15     29
        #         # / \    / \
        #         # 5  10 23 30
        #         #       / \
        #         #      22 25
        #         # delete 20
        #         node_right = node.right
        #         min_node_on_right_side = self.get_min(node_right)
        #         node.value = min_node_on_right_side.value

        #         self.delete_with_value_from_node(
        #             node_right, min_node_on_right_side.value)
        #         return

        #     if node.left is not None:
        #         #  3
        #         # / \
        #         # 2  4
        #         # /
        #         # 1
        #         # delete 2
        #         # 2 = None
        #         #  3
        #         # / \
        #         # 1 4
        #         node = node.left
        #         return node.left
        #     elif node.right is not None:
        #         #  10
        #         # / \
        #         # 8  12
        #         #  \
        #         #    9
        #         # delete 8
        #         # 2 = None
        #         #  10
        #         # / \
        #         # 9 12
        #         node = node.right
        #         return node.right

        # elif node.value > value:
        #     self.delete_with_value_from_node(node.left, value)
        # else:
        #     self.delete_with_value_from_node(node.right, value)

    def get_min(self, node):
        # import pdb
        # pdb.set_trace()

        current_node = node
        while current_node.left is not None:
            current_node = current_node.left

        return current_node

    def delete_node(self, value):
        #   20
        #  /  \
        # 8    29
        # /\  /  \
        # 5  15  23    30
        # /       /
        # 3       22

        self.root = self.delete_node_from(self.root, value)

    def delete_node_from(self, node, value):
        if node.value == value:
            if node.left is None and node.right is None:
                return None

            if node.left is not None and node.right is not None:
                node_right = node.right
                # import pdb
                # pdb.set_trace()
                min_node_on_right_side = self.get_min(node_right)
                node.value = min_node_on_right_side.value

                node.right = self.delete_node_from(
                    node_right, min_node_on_right_side.value)
                return node

            if node.left is not None:
                return node.left
            elif node.right is not None:
                return node.right
        elif node.value > value:
            node.left = self.delete_node_from(node.left, value)
            return node
        else:
            node.right = self.delete_node_from(node.right, value)
            return node

    def _find_node_from(self, node, value):
        if node is None:
            # print("Node is None")
            return (None, False)
        # print("Node {}".format(node.value))
        if node.value == value:
            # print("Found node")
            # print(node)
            return (node, True)
        if node.value > value:
            return self._find_node_from(node.left, value)
        else:
            return self._find_node_from(node.right, value)

    def _insert_with_node(self, node, value):
        if value < node.value:
            if node.left is None:
                node.left = BNode(value)
            else:
                self._insert_with_node(node.left, value)
        else:
            if node.right is None:
                node.right = BNode(value)
            else:
                self._insert_with_node(node.right, value)

    def print_tree(self):
        self.print_node_from(self.root)

    def print_node_from(self, node):
        if node.left is not None:
            self.print_node_from(node.left)
        node.print_node()
        if node.right is not None:
            self.print_node_from(node.right)


class TreeNode():
    def __init__(self, value, children=[]):
        self.value = value
        self.children = children

    def add_child(self, value):
        self.children.append(TreeNode(value))


class BinaryNode:
    def __init__(self, value, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right

    # Tree Traversal

    # 1. Preorder - visit on the node, visit the left, visit the right
    # 2. Post order - visit left, visit right, visit the node
    # 3. Inorder - visit left, visit the node, visit the right

    def print_node(self):

        result = {}
        if self.left is not None:
            result["left"] = self.left.value
        if self.right is not None:
            result["right"] = self.right.value
        result["current_node"] = self.value
        print(result)
        if self.left is not None:
            self.left.print_node()

        print(self.value)

        if self.right is not None:

            self.right.print_node()

    def insert(self, value):
        if value < self.value:
            if self.left is None:
                self.left = BinaryNode(value)
            else:
                self.left.insert(value)
        elif value >= self.value:
            if self.right is None:
                self.right = BinaryNode(value)
            else:
                self.right.insert(value)


class BinaryTree():

    def __init__(self, root=None):

        self.root = root

    def insert(self, value):
        if not self.root:
            self.root = BinaryNode(value)
            return
        self.root.insert(value)

    def find_value(self, value):
        rootNode = BinaryNode(value)

    def print_tree(self):
        if self.root is not None:
            self.root.print_node()


# t = BinaryTree(root=BinaryNode(1))
t = BTree(root=BNode(69))
# random.seed()
# for i in (0, 10):
#     v = int(random.uniform(20, 100))
#     print("Inserting {}".format(v))
#     t.insert(v)
# random.seed()
listt = [19, 70, 99, 94]
for i in listt:
    # v = int(random.uniform(1, 200))
    # print("Inserting {}".format(v))
    # print("Inserting " + str(i))
    t.insert(i)

# t.print_tree()
print("BFS")
print(t.bfs())

find_input = int(input('Enter a value to find: '))
print(t.delete_node(find_input))

print("BFS")
print(t.bfs())

# t.print_tree()

# print("Enter a value to find in the tree:")
# v = int(raw_input())
# print(t.find_node_with_value(v))

# print("DFS")
# print(t.dfs())
print("BFS")
print(t.bfs())

# print("In order")
# t.inorder()
# print("Pre order")
# t.preorder()
# print("Post order")
# t.postorder()


class Heap:
    def __init__(self):
        self.root = None

    def insert(self, value):
        if self.root is None:
            self.root = BNode(value)
            return
