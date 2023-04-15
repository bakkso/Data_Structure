class Stack_411:
    def __init__(self,capacity):
        self.top = []
        self.capacity = capacity
    def __str__(self):
        return str(self.top)
    def isEmpty(self):
        return len(self.top) == 0
    def size(self):
        return len(self.top)
    def push(self,item):
        if len(self.top) == self.capacity:
            print("스택 오버플로우 : 스택이 가득 찼습니다.")
            return # 오류 메세지 출력 후, 항목 추가 중단
        self.top.append(item)
    def pop(self):
        if self.isEmpty():
            print("스택 언더플로우 : 스택이 비어있습니다.")
            return None
        return self.top.pop()
        """ if not self.isEmpty(): 조건문으로 항목이 있는지를 확인하고 있으며, 이 경우 "스택 언더플로우" 오류 메세지 출력하지않음.
        따라서 if not self.isEmpty(): 조건문 제거하고 else문에서 스택 언더플로우 오류 메세지를 출력하도록 해야함.
        if not self.isEmpty():
            return self.top.pop(-1)
        elif len(self.top) == 0:
            print("스택 언더플로우 : 스택이 비어있습니다.")
        """
    def peek(self):
        if not self.isEmpty():
            return self.top[-1]

s = Stack_411(10)

for i in range (0, 15):
    s.push(i)
for i in range(0, 15):
   print(s.pop())
