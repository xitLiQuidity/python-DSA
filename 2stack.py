# 2 stack 
# stack - Filo 
# queue - Fifo 
# queue using two stacks 

class Stack:
    def __init__(self):
        self._items = []

    def push(self, value):
        self._items.append(value)

    def pop(self):
        if not self._items:
            raise IndexError("pop from empty stack")
        return self._items.pop()

    def top(self):
        if not self._items:
            raise IndexError("top from empty stack")
        return self._items[-1]

    def is_empty(self):
        return len(self._items) == 0

    def __len__(self):
        return len(self._items)


class QueueUsingTwoStacks:
    def __init__(self):
        self._in_stack = Stack()
        self._out_stack = Stack()

    def enqueue(self, value):
        self._in_stack.push(value)

    def _transfer_in_to_out(self):
        while not self._in_stack.is_empty():
            self._out_stack.push(self._in_stack.pop())

    def dequeue(self):
        if self._out_stack.is_empty():
            self._transfer_in_to_out()
        if self._out_stack.is_empty():
            raise IndexError("dequeue from empty queue")
        return self._out_stack.pop()

    def peek(self):
        if self._out_stack.is_empty():
            self._transfer_in_to_out()
        if self._out_stack.is_empty():
            raise IndexError("peek from empty queue")
        return self._out_stack.top()

    def is_empty(self):
        return self._in_stack.is_empty() and self._out_stack.is_empty()

    def __len__(self):
        return len(self._in_stack) + len(self._out_stack)

    def display(self):
        if self._out_stack.is_empty():
            self._transfer_in_to_out()
        print("front ->", " ".join(str(item) for item in self._out_stack._items[::-1]), "<- rear")


q = QueueUsingTwoStacks()
q.enqueue(10)
q.enqueue(20)
q.enqueue(30)
print("queue size:", len(q))
print("peek:", q.peek())
q.display()
print("dequeue:", q.dequeue())
print("dequeue:", q.dequeue())
q.enqueue(40)
print("dequeue:", q.dequeue())
print("dequeue:", q.dequeue())
print("is empty:", q.is_empty())
