from queue import Queue
from stack import Stack
from singly_linked_list import SinglyLinkedList
from doubly_linked_list import DoublyLinkedList

singly = SinglyLinkedList()
singly.push(10)
singly.push(20)
singly.push(30)
singly.push(99)
singly.print_list()
singly.print_reverse(singly.head)
print()
singly.reverse()
singly.print_list()




