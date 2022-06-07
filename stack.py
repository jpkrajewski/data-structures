class Stack:
    def __init__(self):
        self.s = []
        self.stack_overflow = 10

    def push(self, number: int):
        if self.is_full():
            raise Exception('Stack overflow')
        self.s.append(number)

    def pop(self) -> int:
        return self.s.pop()

    def top(self) -> int:
        return self.s[-1:][0]

    def size(self) -> int:
        return len(self.s)

    def is_empty(self) -> bool:
        return False if len(self.s) else True

    def is_full(self) -> bool:
        return True if len(self.s) == self.stack_overflow else False
