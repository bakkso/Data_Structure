# 단순연결리스트를 이용하여 큐 구현
class Node:
    def __init__(self, elem, link=None):
        self.data = elem
        self.link = link


class LinkedQueue:
    def __init__(self):
        self.front = None
        self.rear = None

    def isEmpty(self):
        return self.front == None

    def clear(self):
        self.front = None

    def enqueue(self, elem):
        n = Node(elem, None)
        if self.isEmpty():
            self.front = n
            self.rear = n
        else:
            self.rear.link = n
            self.rear = n

    def dequeue(self):
        if not self.isEmpty():
            data = self.front.data
            self.front = self.front.link
            return data
