class ArrayList:
    def __init__(self):
        self.items = []

    def insert(self, pos, elem):
        self.items.insert(pos, elem)

    def delete(self, pos):
        temp = self.items[pos]
        for i in range(pos+1, self.size()):  # pos는 삭제할 위치
            self.items[i-1] = self.items[i]
        self.items[s.size() - 1] = temp
        return self.items.pop(-1)

    def isEmpty(self):
        return self.size() == 0

    def getEntry(self, pos):
        return self.items[pos]

    def size(self):
        return len(self.items)

    def clear(self):
        self.items = []

    def find(self, item):
        return self.items.index(item)

    def replace(self, pos, elem):
        self.items[pos] = elem

    def sort(self):
        self.items.sort()

    # merge()을 extend사용하지않고 insert(), delete()을 이용하여 구현
    def merge(self, lst):
        for i in range(lst.size()):
            self.items.insert(self.size()+1, lst[i])
            lst.delete()

    def display(self, msg='ArrayList:'):
        print(msg, self.size(), self.items)


s = ArrayList()
s.display('파이썬 리스트로 구현한 리스트 테스트')
s.insert(0, 10)
s.insert(0, 20)
s.insert(1, 30)
s.insert(s.size(), 40)
s.insert(2, 50)
s.display("파이썬 리스트로 구현한 List(삽입x5): ")
s.sort()
s.display("파이썬 리스트로 구현한 List(정렬후): ")
s.replace(2, 90)
s.display("파이썬 리스트로 구현한 List(교체x1): ")

s.delete(2)
s.delete(s.size() - 1)
s.delete(0)
s.display("파이썬 리스트로 구현한 List(삭제x3): ")
