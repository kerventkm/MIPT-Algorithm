class ListNode:
    def __init__(self, val, next, prev):
        self.val = val
        self.next = next
        self.prev = prev


class List:
    def __init__(self):
        self.head = ListNode(None, None, None)
        self.tail = ListNode(None, None, self.head)
        self.head.next = self.tail
        self.len = 0

    def insert(self, previous_node, val):
        if not isinstance(previous_node, ListNode):
            raise TypeError("Expected previous_node to be"
                            "ListNode instance")
        if previous_node.next is None:
            raise ValueError('cant add elemen ')
        new_node = ListNode(val, previous_node.next, previous_node)
        previous_node.next.prev = new_node
        previous_node.next = new_node
        self.len += 1
        return new_node

    def remove(self, node):
        if node.next is None or node.prev is None:
            raise IndexError('cant add element'
                             'They are service element')
        node.prev.next = node.next
        node.next.prev = node.prev
        self.len -= 1
        return node

    def push_back(self, val):
        return self.insert(self.tail.prev, val)

    def push_front(self, val):
        return self.insert(self.head, val)

    def pop_back(self):
        return self.remove(self.tail.prev).val

    def pop_front(self):
        return self.remove(self.head.next).val

    def get_node_by_index(self, i):
        if not (0 <= i < self.len + 2):
            raise IndexError('List index out of range')
        res = self.head
        for i in range(i):
            res = res.next
        return res

    def insert_by_index(self, i, val):
        if not isinstance(i, int):
            raise TypeError("Expected i to be integer")
        if i < 0:
            i += self.len + 1
        return self.insert(self.get_node_by_index(i), val)

    def __len__(self):
        # This function is for using len(x).
        return self.len

    def __repr__(self):
        # This function is for visualization.
        # It allows to use print() for List
        show_len = min(len(self), 10)
        elements_repr = list(map(str, [self[i] for i in range(show_len)]))
        if len(self) > 10:
            elements_repr.append('...')
        return f'List({len(self)} elements): [{", ".join(elements_repr)}]'

    def __iter__(self):
        p = self.head.next
        while p.next is not None:
            yield p.val
            p = next(p)

    def __getitem__(self, i):
        if i < 0:
            i += self.len
        if not (0 <= i < len(self)):
            raise IndexError(f'index {i} is out of range'
                             f'for list of size {len(self)}')
        return self.get_node_by_index(i+1).val


# Built in python function
# from collections import deque - doubly linked list

# push_back - O(1)
# pop_back - O(N)
# get - O(N)
# insert - O(1) 
# remove - O(N)
# push_front - O(1)
# pop_front - O(1)
