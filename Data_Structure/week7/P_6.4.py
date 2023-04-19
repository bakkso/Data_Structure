# 이중연결리스트를 사용한 큐 구현

# 이중연결리스트의 노드
class Node:
    def __init__(self, elem, prev=None, next=None):
        self.data = elem
        self.prev = prev
        self.next = next


# 이중연결리스트 - 큐

class DoublyLinkedQueue:
    def __init__(self):
        self.front = None
        self.rear = None

    def isEmpty(self):
        return self.front == None

    # rear에 노드를 추가 : 이중연결리스트의 addRear()활용

    def enqueue(self, item):
        n = Node(item, self.rear, None)
        if (self.isEmpty()):
            self.front = self.rear = n
        else:
            self.rear.next = n
            self.rear = n

    # front에서 노드 제거 및 노드의 data 리턴 -> 이중연결리스트의 deleteFront() 활용

    def dequeue(self):
        if not self.isEmpty():
            data = self.front.data
            self.front = self.front.next
            if self.front == None:
                self.rear = None
            else:
                self.front.prev = None
            return data

    # front 노드의 data만 리턴

    def peek(self):
        if not self.isEmpty():
            data = self.front.data
            return data

    # 출력하고 하나씩 옆으로 이동해야하므로 이중연결리스트의 display()활용

    def display(self, msg='LinkedQueue: '):
        print(msg, end='')
        n = self.front
        while not n == None:
            print(n.data, end=' ')
            n = n.next
        print()


print('연결된 구조의 큐 \n')

queue = DoublyLinkedQueue()

for i in range(10):
    queue.enqueue(i)
queue.display('큐 enqueue 9회: ')

print('\tdequeue() --> ', queue.dequeue())
print('\tdequeue() --> ', queue.dequeue())
print('\tdequeue() --> ', queue.dequeue())
queue.display('큐 enqueue 3회: ')
print('\tpeek() -->', queue.peek())
