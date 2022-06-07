from node import Node


class DoublyLinkedList:
    def __init__(self):
        self.head = None

    def push(self, data):
        self.head = Node(data, self.head)

    def push(self, data):
        if not self.head:
            self.head = Node(data, self.head)
            return

        new_node = Node(data, self.head)
        self.head.prev_node = new_node
        self.head = new_node

    def reverse(self):
        temp = self.head
        while temp.next_node:
            temp = temp.next_node

        self.head = temp

        while temp:
            swap = temp
            temp.next_node = temp.prev_node
            temp.prev_node = swap.next_node
            temp = temp.next_node

    def insert_at_index(self, index: int, data):
        temp = self.head
        if not index:
            self.push(data)
            return

        i = 0
        while index > i:
            temp = temp.next_node
            i += 1

        new_node = Node(data, prev_node=temp.prev_node, next_node=temp)
        temp.prev_node.next_node = new_node
        temp.prev_node = new_node

    def delete_node(self, index: int):
        temp = self.head
        if not index:
            self.head = temp.next_node
            return

        i = 0
        while index > i:
            temp = temp.next_node
            i += 1

        prev_node = temp.prev_node
        next_node = temp.next_node
        prev_node.next_node = next_node
        if not next_node:
            return
        next_node.prev_node = prev_node

    def append(self, data):
        temp = self.head
        while temp.next_node:
            temp = temp.next_node

        temp.next_node = Node(data, prev_node=temp)

    def print_list(self, backwards=False):
        temp = self.head
        print('Travelsal fowards')
        while temp.next_node:
            print(temp.val, end=" ")
            temp = temp.next_node
        print(temp.val)

        if backwards:
            print('Travelsal backwards')
            while temp:
                print(temp.val, end=" ")
                temp = temp.prev_node
            print()