class Queue:
    def __init__(self):
        self.items = []

    def isEmpty(self):
        return len(self.items) == 0

    def enqueue(self, item):
        self.items.append(item)

    def dequeue(self):
        if not self.isEmpty():
            return self.items.pop(0)

    def peek(self):
        if not self.isEmpty():
            return self.items[0]

    def display(self):
        if not self.isEmpty():
            print(self.items)


# 5.15 - 1번
values1 = Queue()
for i in range(20):
    if i % 3 == 0:
        values1.enqueue(i)
values1.display()


# 5.15 - 2번
values2 = Queue()
for i in range(20):
    if i % 3 == 0:
        values2.enqueue(i)
    elif i % 4 == 0:
        values2.dequeue()
values2.display()
