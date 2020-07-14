class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

    def get_value(self):
        return self.value

    def set_value(self, value):
        self.value = value

    def get_next(self):
        return self.next

    def set_next(self, node):
        self.next = node

class LinkedList:
    def __init__(self):
        self.head = None
        self.tail = None
        
    def contains(self, value):
        if not self.head:
            return False
        
        current = self.head
        while current:
            if current.get_value() == value:
                return True
            
            current = current.get_next()
        
        return False

    def get_max(self):
        if not self.head:
            return None
        
        if self.head is self.tail:
            return self.head.get_value()

        current = self.head
        curr_max = current.get_value()

        while current:
            curr_max = max(curr_max, current.get_value())
            current = current.get_next()
        
        return curr_max

    def add_to_tail(self, val):
        node = Node(val)
        if self.head is None:
            self.head = node
            self.tail = node
        else:
            self.tail.set_next(node)
            self.tail = self.tail.get_next()
    
    def prepend(self, val):
        node = Node(val)
        if self.head is None:
            self.head = node
            self.tail = node
        else:
            node.set_next(self.head)
            self.head = node

    def remove_head(self):
        if self.head is None:
            return None
        
        if self.head.get_next() is None:
            head = self.head
            self.head = None
            self.tail = None
        
            return head.get_value()
        
        head = self.head
        self.head = head.get_next()
        return head.get_value()

    def remove_tail(self):
        if self.tail is None:
            return None

        if self.head is self.tail:
            tail = self.tail
            self.head = None
            self.tail = None

            return tail.get_value()
        
        current = self.head
        next_node = current.get_next()
        while next_node.get_next():
            current = next_node
            next_node = current.get_next()
        
        self.tail = current
        self.tail.set_next(None)
        return next_node.get_value()
    


        