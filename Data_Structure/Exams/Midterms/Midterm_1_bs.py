import random


class Node:
    def __init__(self, elem, link=None):
        self.data = elem
        self.link = link


class LinkedList:
    def __init__(self):
        self.head = None

    def isEmpty(self):
        return self.head == None

    def clear(self):
        self.head = None

    def size(self):
        n = self.head
        count = 0
        while not n == None:
            n = n.link
            count += 1
        return count

    def display(self, msg="LinkedStack: "):
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

    def insert(self, pos, elem):
        before = self.getNode(pos-1)
        if before == None:
            self.head = Node(elem, self.head)
        else:
            n = Node(elem, before.link)
            before.link = n

    def findMinMax(self):
        if self.isEmpty():
            return None
        else:
            min = 101
            max = 0
            min_node = None
            max_node = None

            n = self.head

            while not n == None:
                if n.data > max:
                    max_node = n
                    max = n.data
                if n.data < min:
                    min_node = n
                    min = n.data

                n = n.link
        return (min_node, max_node)


s = LinkedList()

for i in range(10):
    s.insert(i, random.randint(1, 100))

s.display("숫자 10개 리스트: ")

minNode, maxNode = s.findMinMax()
print("Min = ", minNode.data, "Max = ", maxNode.data)
