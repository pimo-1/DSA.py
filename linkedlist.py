# Node constructor 
class Node:
    def __init__(self , value):
        self.value = value
        self.next = None
        
# Linked List constructor
class LinkedList:
    def __init__(self , value):
        new_node = Node(value)
        self.head = new_node 
        self.tail = new_node

# Append method
    def append(self , value):
        new_node = Node(value)
        if self.head is None:
            self.head = new_node
            self.tail = new_node
        else:
            self.tail.next = new_node
            self.tail = new_node
            return True

# Pop method 
    def pop(self):
        if self.head is None:
            return None
            
        elif self.head == self.tail:
            self.head = None
            self.tail = None
            return True
        
        else:
            temp = self.head
            while temp.next != self.tail:
                temp = temp.next
            temp.next = None
            self.tail = temp
            return True
            
