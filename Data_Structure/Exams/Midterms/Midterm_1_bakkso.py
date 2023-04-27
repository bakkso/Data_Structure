# 단순 연결 리스트에서 최소값과 최대값을 갖는 노드를 반환하는 함수 findMinMax()작성
# 연결 리스트의 마지막에 1 ~ 100 사이 랜덤 숫자 10개 추가 : randint()함수 사용
# 최소값과 최대값 출력
import random


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

    def findMinMax(self):
        if self.isEmpty():
            return None
        else:
            # 최대값의 인덱스와 최소값을 0번째 노드로 선언
            highest = 0
            lowest = 0
            # 연결리스트의 마지막까지 최대와 최소값을 구하는 것 반복
            # 1번째부터 시작하는 이유 : 0번째를 최대와 최소 인덱스로 잡아줬기때문
            for i in range(1, self.size()):
                # 현재의 i번째 노드의 값이 현재 최대값보다 크다면
                if self.getEntry(i) > self.getEntry(highest):
                    # i의 값을 highest의 인덱스로 업데이트
                    highest = i
                # 현재의 i번째 노드의 값이 현재 최소값보다 작다면
                elif self.getEntry(i) < self.getEntry(lowest):
                    # i의 값을 lowest의 인덱스로 업데이트
                    lowest = i
            # 노드로 반환하라고 했으니까 구해진 최소값과 최댓값의 인덱스에 해당되는 노드를 반환
            return (self.getNode(lowest), self.getNode(highest))


# 클래스 LinkedList을 사용하는 인스턴스 s 선언
s = LinkedList()

# 연결 리스트의 마지막에 1 ~ 100 사이 랜덤숫자 10개 추가
for i in range(10):
    s.insert(i, random.randint(1, 100))

# 추가된 랜덤 숫자 연결리스트 출력
s.display("숫자 10개 리스트: ")

# 연결리스트에서 최소값과 최댓값의 노드를 반환하는 findMinMax()함수를 적용한 s를 각 값에 넣어줌
minNode, maxNode = s.findMinMax()

# findMinMax()는 노드를 반환한거니까 데이터로 확실하게 출력해줌
print("Min = %d, Max = %d" % (minNode.data, maxNode.data))


"""
    def findMinMax(self):
        if self.isEmpty():
            return None
        else:
            highest = 0
            lowest = 0
            for i in range(1, self.size()):
                if self.getEntry(i) > self.getEntry(highest):
                    highest = i
                elif self.getEntry(i) < self.getEntry(lowest):
                    lowest = i

            return (lowest, highest) # 이거는 인덱스 반환이라서 문제 조건에 맞지 않음


s = LinkedList()

for i in range(10):
    s.insert(i, random.randint(1, 100))

s.display("숫자 10개 리스트: ")

minNode, maxNode = s.findMinMax()

# 처음에 노드의 데이터가 출력이 안됐고
# (minNode.data를 해도 안 됐음 -> 아마도 findMinMax()메소드에서 노드가 반환이 안되어서 그런듯, 처음에 인덱스만 반환해줬음)
# return (lowest, highest)로 해줘서 인덱스만 반환됨 -> 문제에서 요구한 조건은 X 
# 다른 방법을 해도 안되었다.
# 결국 지피티의 손을 빌려.. 출력 부분만 손봐줬다.
# 지피티 천재!!
print("Min = ", s.getEntry(minNode), end='')
print(" Max = ", s.getEntry(maxNode))
"""
