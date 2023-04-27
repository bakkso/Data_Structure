# 단순 연결 리스트에서 서로 다른 값의 빈도수를 계산하여 딕셔너리 자료형으로 반환하는 함수 countDiff()작성
# 연결 리스트의 마지막에 1 ~ 10 사이 랜덤 숫자 20개 추가
# 서로 다른 숫자의개수를 X: 0개 형식으로 출력

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

    def display(self, msg="LinkList :"):
        print(msg, end=' ')
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

    def getEntry(self, pos):
        n = self.getNode(pos)
        if n == None:
            return None
        else:
            return n.data

    def find(self, data):
        n = self.head
        while n is not None:
            if n.data == data:
                return n
            n = n.link
        return None
    """
    def countDiff(self):
        d = LinkedList()
        if self.isEmpty():
            return 0
        else :
            count = 0
            n = self.head
            while n != None :
                for i in range(0, self.size()):
                    data = self.getEntry(i)
                    if n.data == data:
                        n = n.link
                        count += 1
                myDict = {self.getEntry(i):count}
                d.insert(i,myDict)
            return d
"""

    def countDiff(self):
        # 반환해줄 딕셔너리 자료형 map 선언
        map = {}
        if self.isEmpty():
            return 0
        else:
            # 초기 count 설정
            count = 0
            # 연결리스트의 마지막 노드까지 빈도수를 계산해야하니까 -> 연결리스트의 길이만큼 for문 반복
            for i in range(0, self.size()):
                # 포인터처럼 사용할 n 선언 & 초기화 (self.head가 가리키고 있는 노드를 가리키도록)
                # 초기화를 해주는 이유 : ex. 2번째 노드의 빈도수를 계산할때 0번째, 1번째 노드들도 2번째 노드와 비교를 하여 빈도수를 계산해야하기때문
                # 이 포인터 n은 연결리스트의 각 노드의 끝까지 돌면서 '기준 노드'와 각 노드들을 비교할때 사용됨
                n = self.head
                # '기준 노드' : 기준 값이 되는 i번째의 노드의 data 따로 저장 (포인터가 변하면 안되니까)
                data = self.getEntry(i)
                # n이 마지막 None을 가리키기 전까지 반복
                while n != None:
                    # 포인터가 현재 가리키고 있는 노드의 data가 기준 노드의 데이터값과 같다면
                    if n.data == data:
                        # count 1을 더해줌
                        count += 1
                    # 다음 노드로 이동
                    n = n.link
                # i번째 노드의 데이터의 값을 key로 그 데이터의 빈도수 계산값을
                # value로 가지는 딕셔너리 자료형으로 딕셔너리 자료형의 변수 myDict을 선언
                myDict = {self.getEntry(i): count}
                # 딕셔너리 자료형인 변수 myDict을 딕셔너리 map에 추가
                map.update(myDict)
                # 빈도수 계산값 count 초기화
                count = 0
            # 최종 빈도수 계산값 딕셔너리 반환
            return map


"""
    def countDiff(self):
        map = {}
        if self.isEmpty():
            return 0
        else :
            count = 0
            n = self.head
            for i in range(0, self.size()):
                data = self.getEntry(i)
                value = self.find(data)
                self.find(data)
                myDict = {self.getEntry(i):count}
                map.update(myDict)
            return map
        
    def find(self,data):
        n = self.head
        while n is not None:
            if n.data == data :
                count += 1
                return count
            n = n.link
        return None
"""

# 클래스 LinkedList을 사용하는 인스턴스 s 선언
s = LinkedList()

# 연결 리스트의 마지막에 1 ~ 10 사이 랜덤숫자 20개 추가
for i in range(0, 20):
    s.insert(i, random.randint(1, 10))

# 추가된 랜덤 숫자 연결리스트 출력
s.display("숫자 20개 리스트: ")

# 연결리스트의 모든 노드에서 서로 다른 값의 빈도수를 계산된 딕셔너리 자료형을 변수 countDict으로 선언
countDict = s.countDiff()

# countDict 출력
print("서로 다른 숫자의 갯수: ", countDict)
