# class MyQueue():

#     def __init__(self):
#         self._data = []

#     def enqueue(self, value):
#         self._data.append(value)

#     def dequeue(self):
#         return self._data.pop(0)

#     def first(self):
#         if self.size() > 0:
#             return self._data[0]
#         return None

#     def empty_queue(self):
#         self._data = []

#     def is_empty(self):
#         return len(self._data) == 0

#     def size(self):
#         return len(self._data)

#     def print_all(self):
#         print(self._data)


class MyQueue2():
    DEFAULT_CAP = 10

    def __init__(self):
        self._data = [None] * self.DEFAULT_CAP
        self._front = 0
        self._size = 0

    def size(self):
        return self._size

    def is_empty(self):
        return self._size == 0

    def first(self):
        if self._size > 0:
            return self._data[self._front]
        return None

    def dequeue(self):

        if self.is_empty():
            return None

        # get data
        data = self._data[self._front]

        # reset index to None
        self._data[self._front] = None

        # [1,2,3, ...None]
        # front=0
        # data = [0] = 1
        # [None,2,3, ...None]

        # advance front
        self._front = (self._front+1) % len(self._data)

        self._size -= 1
        return data

    def enqueue(self, value):

        if self._size == len(self._data):
            self._resize(2*len(self._data))
        # [1]
        back_index = (self._front + self._size) % len(self._data)
        self._data[back_index] = value
        self._size += 1

    def _resize(self, cap):
        old_data = self._data

        new_data = [None] * cap

        old_front = self._front

        for i in range(self._size):
            new_data[i] = old_data[old_front]
            old_front = (old_front + 1) % len(old_data)

        self._data = new_data
        self._front = 0

    def print_all(self):
        print("Front ", self._front)
        print("Size ", self._size)
        print("Data ", self._data)


class Node(object):
    def __init__(self, value, next=None):
        self.value = value
        self.next = next


class LinkedList(object):

    def __init__(self):
        self.head = None

    def size(self):
        total = 0

        current = self.head
        while current is not None:
            total += 1
            current = current.next

        return total

    def print_all(self):

        current = self.head
        while current is not None:
            print(current.value)
            current = current.next

    def add(self, value):

        if self.head is None:
            self.head = Node(value)
            return

        current = self.head
        while current.next is not None:
            current = current.next

        current.next = Node(value)

    def remove_last(self):

        if not self.head:
            return None

        prev = self.head
        current = self.head.next

        if current is None:
            data = self.head.value
            self.head = None
            return data

        while current is not None and current.next is not None:
            prev = current
            current = current.next

        data = current.value
        prev.next = None
        return data


class LinkQueue():
    def __init__(self):
        self._data = LinkedList()

    def enqueue(self, value):
        self._data.add(value)

    def dequeue(self):
        return self._data.remove_last()

    def size(self):
        return self._data.size()

    def is_empty(self):
        return self._data.size() == 0

    def print_all(self):
        self._data.print_all()


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

    def remove_head(self):
        current = self.head

        if current is None:
            return 'Empty list'

        self.head = current.next
        self.size -= 1
        return current.value


class MyQueue:

    def __init__(self):
        self.queue = LinkedList()

    def enqueue(self, data):
        return self.queue.add(data)

    def dequeue(self):
        return self.queue.remove_head()

    def print_queue(self):
        return self.queue.print_all()


class ListQueue:

    def __init__(self):
        self.queue = []

    def enqueue(self, data):
        return self.queue.append(data)

    def dequeue(self):
        return self.queue.pop(0)

    def print_queue(self):
        return print(self.queue)


q = ListQueue()

q.print_queue()
q.enqueue(9)
q.dequeue()
for v in range(1, 5):
    q.enqueue(v)

q.print_queue()
1, 2, 3, 4

q.dequeue()
2, 3, 4

q.print_queue()

q.dequeue()
3, 4

q.print_queue()

q.enqueue(50)

q.print_queue()
3, 4, 50
print(q.dequeue())
4, 50
q.print_queue()
4, 50
