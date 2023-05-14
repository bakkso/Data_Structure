from linkedList import LinkedList


class Term:
    def __init__(self, coef, expo):
        self.expo = expo  # 항의 지수
        self.coef = coef  # 항의 계수


class SparsePoly(LinkedList):
    def __init__(self):
        super().__init__()

    def degree(self):
        return self.size()

    def display(self, msg=""):
        print(msg, end='')
        n = self.head
        while not n == None:
            print("%d x^%d + " % (n.data.coef, n.data.expo), end=' ')
            n = n.link.link
        print()

    def read(self):
        self.clear()
        while True:
            str = list(map(float, input("계수 차수 입력 (종료: -1) : ").split(" ")))
            if str[0] == -1 and str[1] == -1:
                break
            term = Term(str[0], str[1])
            self.insert(self.size(), term)

    def add(self, B):  # 다항식
        C = SparsePoly()  # 더해진 새로운 다항식을 리턴받을 C 선언
        a = self.head
        b = B.head
        while a != None or b != None:
            if a == None or (b != None and a.data.expo < b.data.expo):
                self.insert(C.size(), Term(a.data.expo, a.data.coef))
                self.insert(C.size(), Term(b.data.expo, b.data.coef))
                a = a.link
                b = b.link
            elif a == None or (b != None and a.data.expo == b.data.expo):
                elem = Term(a.data.expo, a.data.coef+b.data.coef)
                self.insert(C.size(), elem)
                a = a.link
                b = b.link
            else:
                self.insert(C.size(), Term(b.data.expo, b.data.coef))
                self.insert(C.size(), Term(a.data.expo, a.data.coef))
                a = a.link
                b = b.link
        return C

    def insert(self, pos, elem):
        before = self.getNode(pos-1)
        if before == None:
            self.head = LinkedList.Node(elem, self.head)
        else:
            n = LinkedList.Node(elem, before.link)
            before.link = n


a = SparsePoly()
b = SparsePoly()

a.read()
a.display("입력 다항식 : ")

b.read()
b.display("입력 다항식 : ")

c = a.add(b)

a.display("A(x) = ")
b.display("B(x) = ")
#c.display("A + B = ")
