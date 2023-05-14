class Entry:
    def __init__(self, key, value):
        self.key = key
        self.value = value

    def __str__(self):
        if self.key == '-1':
            return str("%s" % self.key)
        else:
            return str("%s:%s" % (self.key, self.value))


class Node:
    def __init__(self, elem, link=None):
        self.data = elem
        self.link = link


class HashLinearMap:
    def __init__(self, M):
        self.table = [None]*M
        self.M = M

    def hashFn(self, key):  # 키를 숫자로 바꾸기 위해서 무조건 필요한 함수
        sum = 0
        for c in key:
            sum = sum + ord(c)
        return sum % self.M

    def quad(self, key, i):  # 충돌났을 때 필요한 함수
        hk = self.hashFn(key)
        q = (hk + i*i) % self.M

        return q

    def insert(self, key, value):
        i = 0

        if self.table is None:
            idx = self.hashFn(key)
        else:
            for i in range(0, (self.M-1)):
                q = self.quad(key, i)
                if self.table[q] is None:
                    idx = self.quad(key, i)
                    break
        self.table[idx] = Node(Entry(key, value), self.table[idx])

    def search(self, key):
        i = 0
        idx = self.hashFn(key)

        while self.table[idx] is not (None):
            if self.table[idx].data.key == key:
                return self.table[idx].data
            else:
                idx = self.quad(key, i)

            if i > self.M:
                break
            else:
                i += 1

        return None

    def delete(self, key):
        i = 0
        idx = self.hashFn(key)

        while self.table[idx] is not (None):
            if self.table[idx].data.key == key:
                self.table[idx].data.key = '-1'
                self.table[idx].data.value = '-1'
                break
            else:
                q = self.quad(key, i)
                idx = self.quad(key, i)

            if i > self.M:
                break
            else:
                i += 1

        return None

    def display(self, msg):
        print(msg)
        for idx in range(len(self.table)):
            n = self.table[idx]
            if n is not None:
                print("[%2d] -> %s" % (idx, self.table[idx].data))
            elif n is None:
                print("[%2d] -> None" % idx)


map = HashLinearMap(13)

map.insert('data', '자료')
map.insert('structure', '구조')
map.insert('sequential search', '선형 탐색')
map.insert('game', '게임')
map.insert('binary search', '이진 탐색')
map.display("나의 단어장: ")

print(" 탐색:game —> ", map.search('game'))
print(" 탐색:over —> ", map.search('over'))
print(" 탐색:data —> ", map.search('data'))

map.delete('game')

map.display("나의 단어장: ")

print(" 탐색:game —> ", map.search('game'))
