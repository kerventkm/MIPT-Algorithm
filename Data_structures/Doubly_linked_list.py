class Linked_node():
    def __init__(self, value, prev, next):
        self.value = value
        self.prev = prev
        self.next = next
        
    def __prev__(self):
        return self.prev
        
    def __next__(self):
        return self.next
    
    def get_value(self):
        return self.value
    
    
class Linked_list():
    def __init__(self):
        self.head = None
        self.tail = None
        self.len = 0
        
    def push_front(self, value):
        new_node = Linked_node(value, None, self.head)
        self.head = new_node
        if self.tail is None:
            self.tail = new_node
        self.len += 1
        
    def insert(self, previous_node, value):
        if not isinstance(previous_node, Linked_node):
            raise TypeError("Expected previous_node to be a Linked_node instance")
        new_node = Linked_node(value, previous_node.next)
        self.len += 1
        if new_node.next is None:
            self.tail = new_node
        return new_node
    
    def push_back(self, value):
        return self.insert(self.tail, value)
    
    def get_node_by_index(self, i):
        if not (0 <= i < self.len):
            raise IndexError("List index out of range")
        res = self.head
        for _ in range(i):
            res = next(res)
        return res
    
    def insert_by_index(self, i, value):
        if isinstance(i, int):
            if i < 0:
                i += self.len + 1
            elif i == 0:
                return self.push_front(value)
            else:
                prev_node = self.get_node_by_index(i-1)
                return self.insert(prev_node, value)
        else:
            TypeError("Expected an integer")
            
    def __len__(self):
        return self.len
    
    def __getitem__(self, i):
        return self.get_node_by_index(i).value
    


# Built in python function
# from collections import deque - doubly linked list

# push_back - O(1)
# pop_back - O(1)
# get - O(N)
# insert - O(1) 
# remove - O(1)
# push_front - O(1)
# pop_front - O(1)
