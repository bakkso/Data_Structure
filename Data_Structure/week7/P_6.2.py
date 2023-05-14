# 연결된 리스트 클래스에 merge()연산 구현
# 연산결과 리스트 A의 길이는 늘어나고, B의 길이는 0이 되도록
class Node:
    def __init__(self, elem, link=None):
        self.data = elem
        self.link = link


class LinkedList:
    def __init__(self):
        self.head = None

    def isEmpty(self): return self.head == None
    def clear(self): self.head = None

    def size(self):
        n = self.head
        count = 0
        while not n == None:
            n = n.link
            count += 1
        return count

    def display(self, msg='LinkedList:'):
        print(msg, end='')
        n = self.head
        while not n == None:
            print(n.data, end=' ')
            n = n.link
        print()

    def getNode(self, pos):
        if pos < 0:
            return None
        n = self.head
        while pos > 0 and n != None:
            n = n.link
            pos -= 1
        return n

    def getEntry(self, pos):
        n = self.getNode(pos)
        if n == None:
            return None
        else:
            return n.data

    def replace(self, pos, elem):
        n = self.getNode(pos)
        if n != None:
            n.data = elem

    def find(self, data):
        n = self.head
        while n is not None:
            if n.data == data:
                return n
            n = n.link
        return n

    def insert(self, pos, elem):
        before = self.getNode(pos-1)
        if before == None:
            self.head = Node(elem, self.head)
        else:
            n = Node(elem, before.link)
            before.link = n

    def delete(self, pos):
        before = self.getNode(pos-1)
        if before == None:
            if self.head is not None:
                self.head = self.head.link
        elif before.link != None:
            before.link = before.link.link

    def merge(self, B):
        n = self.getNode(self.size()-1)
        n.link = B.head
        B.head = None


a = LinkedList()
b = LinkedList()

a.insert(0, 1)
a.insert(1, 2)
a.insert(2, 3)

b.insert(0, 4)
b.insert(1, 5)
b.insert(2, 6)

a.display("A의 LinkedList : ")
b.display("B의 LinkedList : ")

a.merge(b)

a.display("A의 LinkedList : ")
b.display("B의 LinkedList : ")

print(a.size())
print(b.size())
