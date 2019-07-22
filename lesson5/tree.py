import random


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

    def print_inorder_node(self):

        # result = {}
        # if self.left is not None:
        #     result["left"] = self.left.value
        # if self.right is not None:
        #     result["right"] = self.right.value
        # result["current_node"] = self.value
        # print(result)
        if self.left is not None:
            self.left.print_inorder_node()
        print(self.value)

        if self.right is not None:
            self.right.print_inorder_node()

    def print_pre_order(self):
        # result = {}
        # if self.left is not None:
        #     result["left"] = self.left.value
        # if self.right is not None:
        #     result["right"] = self.right.value
        # result["current_node"] = self.value
        # print(result)

        print(self.value)

        if self.left is not None:
            self.left.print_pre_order()

        if self.right is not None:
            self.right.print_pre_order()

    def descending_order(self):

        result = {}
        if self.left is not None:
            result["left"] = self.left.value
        if self.right is not None:
            result["right"] = self.right.value
        result["current_node"] = self.value
        print(result)

        if self.right is not None:
            self.right.descending_order()

        print(self.value)

        if self.left is not None:
            self.left.descending_order()

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

    def print_tree_pre_order(self):
        if self.root is not None:
            self.root.print_pre_order()

    def print_tree_in_order(self):
        if self.root is not None:
            self.root.print_inorder_node()

    def print_tree_descending_order(self):
        if self.root is not None:
            self.root.descending_order()


t = BinaryTree(root=BinaryNode(1))
random.seed()
for i in (0, 10):
    v = int(random.uniform(20, 100))
    print("Inserting {}".format(v))
    t.insert(v)
random.seed()
for i in range(11, 20):
    v = int(random.uniform(1, 200))
    print("Inserting {}".format(v))
    t.insert(v)
t.print_tree_pre_order()
print('BREAK!')
t.print_tree_in_order()
print('BREAK!')
t.print_tree_descending_order()
