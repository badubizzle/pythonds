class Node(object):

    def __init__(self, value, next=None):
        self.value=value
        if isinstance(next, Node):
            self.next=next
        else:
            self.next = None        
    

class LinkedList(object):

    def __init__(self):
        self.root = None
    
    def add(self, node):
        if self.root is None:
            self.root = node
            return
        
        current = self.root
        while current.next is not None:
            current = current.next
        
        current.next = node
    
    def print_all(self):
        current = self.root
        while current is not None:
            print(current.value)
            current = current.next

    def insert_at(self, value, index):
        
        
        node = Node(value)        
        current = self.root

        # 1->2->3
        # insert 4  at index 2


        # index = 2
        # count = 1
        # current = 1
        # current.next = 2 is not None

        # index = 2
        # count = 2
        # current = 2
        # current.next = 3, not None

        # index == count , True
        # 4->3
        # 2->4->3




        if index == 0:
            if self.root is None:
                self.root = node
                return
            node.next = self.root
            return

        count = 1
        while current is not None and current.next is not None:
            if index == count:                
                node.next = current.next
                current.next = node
                return

            current = current.next 
            count = count + 1
        
        current.next = node
        
        

    def find_at_index(self, index):

        current = self.root
        count = 0 # counter to point to index
        while current is not None:
            if index == count:
                return current.value
            count = count + 1
            current = current.next
        
        return None
        

l = LinkedList()
for v in range(0, 10):
    # node = Node(v+1)
    # l.add(node)
    l.insert_at(v+1, v)

print(l.find_at_index(3))
l.print_all()

