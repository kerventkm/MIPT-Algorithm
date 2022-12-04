class Linked_node():
    def __init__(self, value, next):
        self.value = value
        self.next = next
        
    def __next__(self):
        return self.value
    
    def get_value(self):
        return self.value
    
    
class Linked_list():
    def __init__(self):
        self.head = None
        self.tail = None
        self.len = 0
        
    