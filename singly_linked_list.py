from node import Node


class SinglyLinkedList:
    def __init__(self):
        self.head = None

    def push(self, data):
        self.head = Node(data, self.head)

    def insert_at_index(self, index: int, data):
        temp = self.head
        if not index:
            self.push(data)
            return
        i = 1
        while index > i:
            temp = temp.next_node
            i += 1
        new_node = Node(data, temp.next_node)
        temp.next_node = new_node

    def append(self, data):
        temp = self.head
        while temp.next_node:
            temp = temp.next_node
        temp.next_node = Node(data)

    def delete_node(self, index: int):
        if not index:
            self.head = self.head.next_node
            return

        i = 1
        temp = self.head
        while index > i:
            temp = temp.next_node
            i += 1

        node_to_del = temp.next_node
        next_node = node_to_del.next_node
        temp.next_node = next_node

    def print_reverse(self, head):
        if not head:
            return
        self.print_reverse(head.next_node)
        print(head.val, end=' ')

    def reverse(self):
        head = self.head
        prev = None
        while head:
            next_node = head.next_node
            head.next_node = prev
            prev = head
            head = next_node

        self.head = prev

    def __len__(self) -> int:
        if not self.head:
            return 0

        i = 1
        temp = self.head
        while temp.next_node:
            temp = temp.next_node
            i += 1
        return i

    def print_list(self):
        temp = self.head
        while temp:
            print(temp.val, end=" -> ")
            temp = temp.next_node
        print('NULL')
