class Node(object):

    def __init__(self, value, next=None):
        self.value = value
        if isinstance(next, Node):
            self.next = next
        else:
            self.next = None


class LinkedList(object):

    def __init__(self, head=None):
        if isinstance(head, Node):
            self.head = head
        else:
            self.head = None

    def add(self, value):

        # if linked list is empty then
        # make this the head
        if self.head is None:
            # create a new node with value
            # set head to new node
            new_node = Node(value)
            self.head = new_node
            return

        # if list is not empty
        # check next node till next node is None
        # attach new node as next

        # head = 1
        pointer = self.head

        # 1->2->3
        # add 4

        # set pointer = 1
        # check, does 1 has next? Yes
        # set pointer = 2, i.e 1->2
        # check, does 2 has next? Yes
        # set pointer = 3, i.e 2->3
        # check does 3 has next? No
        # pointer(3) -> new_node(4)

        while pointer.next is not None:
            pointer = pointer.next

        new_node = Node(value)
        pointer.next = new_node

    def print_all(self):
        # 1->2->3

        # pointer = 1
        # check, is pointer None? No
        # print(1)
        # set pointer = pointer.next 1->2 => 2

        # check, is pointer None? No
        # print(2)
        # set pointer = pointer.next 2->3 => 3

        pointer = self.head

        while pointer is not None:
            print(pointer.value)
            pointer = pointer.next

    def insert_at(self, value, index):
        node = Node(value)
        current = self.head

        if self.head is None:
            self.head = node
            return
        if index == 0:
            node.next = self.head
            self.head = node
            return

        count = 1

        while current is not None and current.next is not None:
            if count == index:
                node.next = current.next
                current.next = node
                return

            current = current.next
            count += 1

        current.next = node
        return

    def find_at_index(self, index):
        # take a zero based index and return the value of the Node
        # at the index
        # linked_list.find_at_index(0) should return First node's value

        count = 0

        # 1->2->3 => find_at_index(0) should return 1, find_at_index(2) -> 3

        # pointer = 1
        # count = 0
        # check, is index == count?NO
        # set pointer = pointer.next
        # count += 1

        pointer = self.head

        while pointer is not None:
            if count == index:
                return pointer.value
            else:
                pointer = pointer.next
                count += 1

    def find_value(self, value):
        current = self.head

        # value = 4
        # is 2 == 1 returns False
        # set current value to next value
        # 1->2->3
        # check first value

        if current is None:
            return False

        if value == current.value:
            return True

        while current.next is not None:
            current = current.next
            if current.value == value:
                return True
        return False


l = LinkedList()
for v in range(0, 20):
    l.add(v+1)

print(l.find_value(19))
