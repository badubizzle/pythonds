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


class TreeList():

    def __init__(self, data=[]):
        self.root = None
        # self.data = data
        self.build_tree(data)

    def build_tree(self, data):
        if len(data) == 0:
            return 'Empty list'

        self.root = BNode(value=data[0])

        current_index = 0
        current_node = self.root

        queue = []

        left_index = (2 * current_index) + 1
        right_index = (2 * current_index) + 2

        while left_index < len(data):
            current_node.left = BNode(value=data[left_index])
            queue.append(current_node.left)

            if right_index < len(data):
                current_node.right = BNode(value=data[right_index])
                queue.append(current_node.right)

            current_index += 1
            left_index = (2 * current_index) + 1
            right_index = (2 * current_index) + 2

            if len(queue) != 0:
                current_node = queue.pop(0)

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


values = [1, 2, 3, 4, 7, 9, 10, 8, 16, 14, 9, 50]


new_treelist = TreeList(values)

print(new_treelist.bfs())
