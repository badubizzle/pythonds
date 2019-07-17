
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
        self.value=value
        if isinstance(next, Node):
            self.next=next
        else:
            self.next = None        
    

class LinkedList(object):

    def __init__(self, head=None):
        if isinstance(head, Node):
            self.head = head
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
    
    
    
class LinkedStack():

    def __init__(self):
        self.linked_list = LinkedList()
    
    def pop(self):
        """
        Get the top element in the stack
        """
                

    def push(self, value):
        """
        Add to top of stack
        """
        self.linked_list.add(value)        
    
    def empty(self):
        pass
    
    def print_all(self):
        self.linked_list.print_all()


stack = LinkedStack()

for v in range(0, 20):
    stack.push(v+1)

stack.print_all()

