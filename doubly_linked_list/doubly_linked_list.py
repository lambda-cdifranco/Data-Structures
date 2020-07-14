"""
Each ListNode holds a reference to its previous node
as well as its next node in the List.
"""
class ListNode:
    def __init__(self, value, prev=None, next=None):
        self.prev = prev
        self.value = value
        self.next = next

    def delete(self):
        next_node = self.next
        prev_node = self.prev
        if next_node:
            next_node.prev = prev_node
        if prev_node:
            prev_node.next = next_node

        return self
            
"""
Our doubly-linked list class. It holds references to 
the list's head and tail nodes.
"""
class DoublyLinkedList:
    def __init__(self, node=None):
        self.head = node
        self.tail = node
        self.length = 1 if node is not None else 0

    def __len__(self):
        return self.length
    
    def increment(self):
        self.length += 1
    
    def decrement(self):
        self.length -= 1
    
    """
    Wraps the given value in a ListNode and inserts it 
    as the new head of the list. Don't forget to handle 
    the old head node's previous pointer accordingly.
    """
    def add_to_head(self, value):
        node = ListNode(value)
        if not self.head:
            self.head = node
            self.tail = node
        else:
            self.head.prev = node
            node.next = self.head
            self.head = node
        self.increment()
        
    """
    Removes the List's current head node, making the
    current head's next node the new head of the List.
    Returns the value of the removed Node.
    """
    def remove_from_head(self):
        if not self.head:
            return None

        head = self.head

        if self.head is self.tail:
            self.head = None
            self.tail = None
            self.decrement()
            return head.value
            
        next_node = self.head.next
        next_node.prev = None
        self.head = next_node
        self.decrement()

        return head.value
    """
    Wraps the given value in a ListNode and inserts it 
    as the new tail of the list. Don't forget to handle 
    the old tail node's next pointer accordingly.
    """
    def add_to_tail(self, value):
        node = ListNode(value)
        if self.tail is None:
            self.tail = node
            self.head = node
        else:  
            self.tail.next = node
            node.prev = self.tail
            self.tail = node
        self.increment()
            
    """
    Removes the List's current tail node, making the 
    current tail's previous node the new tail of the List.
    Returns the value of the removed Node.
    """
    def remove_from_tail(self):
        if not self.tail:
            return None

        tail = self.tail
        if self.tail is self.head:
            self.head = None
            self.tail = None
            self.decrement()
            return tail.value

        new_tail = self.tail.prev
        new_tail.next = None
        self.tail = new_tail

        self.decrement()
        return tail.value
            
    """
    Removes the input node from its current spot in the 
    List and inserts it as the new head node of the List.
    """
    def move_to_front(self, node):
        if node is self.head:
            return None

        node.delete()
        node.next = self.head
        self.head.prev = node
        self.head = node
        
    """
    Removes the input node from its current spot in the 
    List and inserts it as the new tail node of the List.
    """
    def move_to_end(self, node):
        if node is self.tail:
            return None
        
        if node is self.head:
            self.head = node.next
        
        node.delete()
        node.prev = self.tail
        node.next = None
        self.tail.next = node
        self.tail = node


    """
    Deletes the input node from the List, preserving the 
    order of the other elements of the List.
    """
    def delete(self, node):
        if node is self.tail:
            self.tail = node.prev
        if node is self.head:
            self.head = node.next

        node.delete()
        self.decrement()

    """
    Finds and returns the maximum value of all the nodes 
    in the List.
    """
    def get_max(self):
        if not self.head:
            return None
        
        if self.head is self.tail:
            return self.head.value
        
        current = self.head
        curr_max_val = current.value
        while current is not None:
            current = current.next
            if current is not None:
                curr_max_val = max(current.value, curr_max_val)
        
        return curr_max_val
