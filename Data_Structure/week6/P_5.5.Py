class PQueueSorted:
    def __init__(self):
        self.items = []

    def isEmpty(self):
        return len(self.items) == 0

    def size(self): return len(self.items)
    def clear(self): self.items = []

    def enqueue(self, item):
        self.items.append(item)
        self.items.sort()

    def dequeue(self):
        if not self.isEmpty():
            return self.items.pop(-1)

    def peek(self):
        if not self.isEmpty():
            return self.items[-1]


q = PQueueSorted()
q.enqueue(10)
q.enqueue(34)
q.enqueue(18)
print("Peek Max Priority =  ", q.peek())
q.enqueue(27)
q.enqueue(45)
q.enqueue(15)
print("PQueue: ", q.items)
while not q.isEmpty():
    print("Dequeue Max Priority = ", q.dequeue())
