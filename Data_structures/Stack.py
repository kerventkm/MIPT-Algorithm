class Stack():
    def __init__(self, max_len):
        self.data = [None] * max_len
        self.len = 0
    
    def push(self, value):
        self.data[self.len] = value
        self.len += 1
    
    def front(self):
        return self.data[self.len - 1]
    
    def pop(self):
        res = self.front()
        self.len -= 1
        return res
    
    def clear(self):
        self.len = 0
    
    def __len__(self):
        return self.len


# we can use normal list and apply these functions