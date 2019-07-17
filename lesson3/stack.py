
class MyStack(object):

    def __init__(self):
        self.data = []

    def pop(self):
        self.data.pop()

    def push(self, value):
        self.data.append(value)

    def empty(self):
        len(self.data) == 0

    def size(self):
        len(self.data)


class Node(object):

    def __init__(self, value, next=None):
        self.value = value
        if isinstance(next, Node):
            self.next = next
        else:
            self.next = None


class LinkedList(object):

    def __init__(self, head=None):
        self.size = 0
        if isinstance(head, Node):
            self.head = head
            self.size = 1
        else:
            self.head = None

    def add(self, value):
        if self.head is None:
            new_node = Node(value)
            self.head = new_node
            return

        pointer = self.head
        while pointer.next is not None:
            pointer = pointer.next

        new_node = Node(value)
        pointer.next = new_node

    def print_all(self):
        current = self.head
        while current is not None:
            print(current.value)
            current = current.next

    def add_head(self, value):
        node = Node(value)

        node.next = self.head
        self.head = node
        self.size += 1

    def remove_head(self):
        current = self.head

        if current is None:
            return 'Empty list'

        self.head = current.next
        self.size -= 1
        return current.value


class LinkedStack():

    def __init__(self):
        self.linked_list = LinkedList()

    def pop(self):
        """
        Get the top element in the stack
        """
        return self.linked_list.remove_head()

    def push(self, value):
        """
        Add to top of stack
        """
        self.linked_list.add_head(value)

    def empty(self):
        pass

    def print_all(self):
        self.linked_list.print_all()


stack = LinkedStack()

for v in range(0, 5):
    stack.push(v+1)

# stack.print_all()
stack.pop()
stack.pop()
stack.pop()
stack.print_all()
