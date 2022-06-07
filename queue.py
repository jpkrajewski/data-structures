class Queue:
    def __init__(self):
        self.q = []

    def enqueue(self, number: int):
        self.q.append(number)

    def dequeue(self) -> int:
        return self.q.pop(0)

    def size(self) -> int:
        return len(self.q)

    def is_empty(self) -> bool:
        return False if len(self.q) else True

    def front(self) -> int:
        return self.q[0]

    def rear(self) -> int:
        return self.q[-1:][0]
