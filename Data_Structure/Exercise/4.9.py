class Stack:
    def __init__(self):
        self.top = []

    def __str__(self):
        return str(self.top)

    def isEmpty(self):
        return len(self.top) == 0

    def size(self):
        return len(self.top)

    def push(self, item):
        self.top.append(item)

    def pop(self):
        if not self.isEmpty():
            return self.top.pop(-1)

    def peek(self):
        if not self.isEmpty():
            return self.top[-1]

    # 순환함수로 구현
    def display1(self):
        if self.isEmpty():  # 종료조건
            return
        item = self.pop()
        print(item)
        return self.display1()  # 재귀호출

    def display2(self):
        if not len(self.top):  # 종료조건
            return
        item = self.pop()
        print(item)
        return self.display2()  # 재귀호출
