class Queue():
    def __init__(self, max_len):
        self.data = [None] * max_len
        self.first = 0
        self.last = 0
        self.len = 0
        
    def push(self, value):
        self.data[self.last] = value
        self.last += 1
        self.len += 1
        if self.last == self.max_len:
            self.last = 0    
    
    def front(self):
        if self.len > 0:
            return self.data[self.first]
        else:
            raise IndexError
    
    def pop(self):
        res = self.front()
        self.first += 1
        self.len -= 1
        if self.last == self.max_len:
            self.last = 0
        return res
    
    def clear(self):
        self.first = 0
        self.last = 0
        self.len = 0
    
    def __len__(self):
        return self.len
