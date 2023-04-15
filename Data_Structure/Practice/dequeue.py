class Deque():
    def __init__(self):
        self.items = []

    def isEmpty(self):
        return len(self.items) == 0

    def addFront(self, item):
        self.items.insert(0, item)

    def addRear(self, item):
        self.items.append(item)

    def deleteFront(self):
        if not self.isEmpty():
            return self.items.pop(0)

    def deleteRear(self):
        if not self.isEmpty():
            return self.items.pop(-1)

    # 원형 덱이 아닌 일반 선형 덱임을 꼭 기억하자! 선형 덱은 items[0]부터 요소가 삽입된다.
    def getFront(self):
        if not self.isEmpty():
            return self.items[0]

    def getRear(self):
        if not self.isEmpty():
            return self.items[-1]

    def size(self):
        return len(self.items)

    def display(self):
        print(self.items)
