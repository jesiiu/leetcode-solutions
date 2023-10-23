#232. Implement Queue using Stacks
class MyQueue:

    def __init__(self):
        self.queue = []

    def push(self, x: int) -> None:
        self.queue.append(x)

    def pop(self) -> int:
        value = self.queue[0]
        self.queue = self.queue[1:]
        return value

    def peek(self) -> int:
        return self.queue[0]

    def empty(self) -> bool:
        if len(self.queue) == 0:
            return True
        return False
    
queue = MyQueue()
queue.push(11)
queue.pop()
print(queue.empty())
print()