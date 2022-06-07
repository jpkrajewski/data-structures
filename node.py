class Node:
    def __init__(self, data, next_node=None, prev_node=None):
        self.val = data
        self.next_node = next_node
        self.prev_node = prev_node

    def __str__(self):
        return str(self.val)
    