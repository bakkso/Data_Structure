from linkedList import LinkedList


# 하나의 항은 Term클래스(계수, 차수)로 구현
class Term:
    def __init__(self, coef, expo):
        self.expo = expo  # 항의 지수
        self.coef = coef  # 항의 계수


# 희소다항식의 클래스, 연결된 리스트(LinkedList)상속받아서 사용
class SparsePoly(LinkedList):
    def __init__(self):
        super().__init__()

    def degree(self):
        if self.size() == 0:
            return 0
        return self.size()

    # LinkedList의 display()활용, 그러나 출력하는 내용이 살짝 수정되어야하니까 그대로 상속받아서 사용은 하지 않는다.

    def display(self, msg=""):
        print(msg, end='')
        n = self.head
        while not n == None:
            print("%s x^%d + " % (n.data.coef, n.data.expo),
                  end=' ')  # 문자열로 받으려면 %s, 정수로 받으려면 %d
            n = n.link
        print()

    def read(self):
        # 다른 다항식을 받기 전 clear로 초기화해준다.
        self.clear()
        while True:
            # 계수와 차수를 스페이스바를 기준으로 나눠서 받는다. map사용->(계수, 차수) 묶어서 받음
            # 문제에서 실수로 받고있으니까 float로 형변환 해준다.
            poly = list(map(float, input("계수 차수 입력 (종료: -1) : ").split(" ")))
            # poly[0]은 계수, poly[1]는 차수 -> 각각 -1을 입력받으면 종료한다.
            if poly[0] == -1 and poly[1] == -1:
                break
            # term에 Term노드의 각각 계수와 차수를 삽입
            term = Term(poly[0], poly[1])
            # 완료된 term(Term노드)를 다항식에 삽입해주고 이 함수는 끝
            # 삽입할 위치는 항상 직전 노드의 다음에 삽입되니까 self.size()를 사용하여 그 다항식 길이의 젤 마지막에 삽입하게 된다.
            # self.insert()를 상속받아 사용함으로써 Node의 link를 사용할 수 있게 됨. ( 따로 Node 선언 불필요 )
            self.insert(self.size(), term)

    def add(self, B):  # self에 B를 더함
        c = SparsePoly()  # 더해진 새로운 다항식을 리턴받을 C 선언
        a = self.head
        b = B.head

        while a != None or b != None:

            # if - a는 이미 traversal(횡단)이 끝났거나, b가 a보다 지수가 큰 상황
            if a == None or (b != None and a.data.expo < b.data.expo):
                # b를 직접 대입
                c.insert(c.size(), Term(b.data.coef, b.data.expo))
                # b만 대입했으니까 a는 이동 x
                b = b.link

            # elif - b는 이미 traversal(횡단)이 끝났거나, a가 b보다 지수가 큰 상황
            elif b == None or (a != None and a.data.expo > b.data.expo):
                # a를 직접 대입
                c.insert(c.size(), Term(a.data.coef, a.data.expo))
                # a만 대입했으니까 b는 이동 x
                a = a.link

            # else - 같으니까 계수는 합해서(coefficient), 지수는 그대로(exponenet)
            else:
                # a와 b의 계수를 더하고 지수는 그대로 냅둔 Term을 elem이라는 변수로 저장
                elem = Term(a.data.coef+b.data.coef, b.data.expo)
                c.insert(c.size(), elem)
                # a와 b모두 비교했으므로 둘다 link
                a = a.link
                b = b.link
        return c

        """_summary_
            while a != None or b != None :
                if a == None or (b != None and a.data.expo < b.data.expo):
                    c.insert(c.size(), Term(b.data.coef, b.data.expo))
                    b = b.link
                elif a == None or (b != None and a.data.expo == b.data.expo):
                    elem = Term(a.data.coef+b.data.coef, b.data.expo)
                    c.insert(c.size(), elem)
                    a = a.link
                    b = b.link
                else:
                    c.insert(c.size(), Term(a.data.coef, a.data.expo))
                    a = a.link
            return c
        Args:
            B (_type_): _description_
        """


a = SparsePoly()
b = SparsePoly()

a.read()
a.display("         입력 다항식 : ")

b.read()
b.display("         입력 다항식 : ")


a.display("         A(x) = ")
b.display("         B(x) = ")

c = a.add(b)  # add가 계속 출력이 안 됐던 이유는 add의 문제가 아니라 display의 문제였다.

c.display("         A + B = ")
# display에서 self.insert를 하여 애꿎은 곳에 insert를 하여 c가 알지못했다.
# display내의 self.insert를 모두 c.insert로 변경해주니 정상적으로 출력되었다.
