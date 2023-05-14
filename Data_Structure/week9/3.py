class Entry:
    def __init__(self, key, value):
        self.key = key
        self.value = value

    def __str__(self):
        return str("%s:%s" % (self.key, self.value))


class BinaryMap:
    def __init__(self):
        self.table = []

    def size(self):
        return len(self.table)

    def display(self, msg=""):
        print(msg)
        for entry in self.table:
            print("  ", entry)

    def insert(self, key, value):
        self.table.append(Entry(key, value))

    def delete(self, key):
        for i in range(self.size()):
            if self.table[i].key == key:
                self.table.pop(i)
                return

    def binary_search(self, key, low, high):
        if (low <= high):
            middle = (low + high) // 2
            if key == self.table[middle].key:
                return middle
            elif (key < self.table[middle].key):
                return self.binary_search(self, key, low, middle-1)
            else:
                return self.binary_search(self, key, middle+1, high)
        return None

    def sort(self):
        n = len(self.table)
        for i in range(n-1, 0, -1):
            bChanged = False
            for j in range(i):
                if (self.table[j] > self.table[j+1]):
                    self.table[j], self.table[j +
                                              1] = self.table[j+1], self.table[j]
                    bChanged = True
            if not bChanged:
                break

    def serch(self, key):
        pos = self.binary_search(self.table, key, 0, self.size()-1)
        if pos is not None:
            return self.table[pos]
        else:
            return None

    def myLineEditor(self):
        while True:
            command = input("이름을 입력하세요(q-종료): ")
            if command == 'q':
                return
            else:
                # 입력받은 이름을 키(key)로, None을 값(value)으로 하는 Entry 객체 생성
                e = Entry(command, None)
                # BinaryMap에서 해당 키(key)를 검색하여 결과 출력
                result = self.search(e.key)
                if result is not None:
                    print("학생을 찾았습니다.")
                    print(result.key, result.value)
                else:
                    print("찾는 학생이 없습니다.")


print("출석부 (정렬전): ")

b = BinaryMap()


with open("namebook.txt", "r") as f:
    for line in f:
        line = line.strip()
        name, id = line.split(":")
        b.insert(name, id)


b.display()


print("출석부 (정렬후): ")

b.sort()

b.display()

b.myLineEditor()


with open("namebook.txt", "r") as f:
    for line in f:
        line = line.strip()
        name, id = line.split()
        b.insert(name, id)
