class Polynomial:
    def __init__(self):
        self.items = []

    def degree(self):  # 다항식의 차수를 반환
        return len(self.items)

    def display(self, msg="f(x) = "):  # 현재 다항식 출력
        print(msg, end='')
        for i in reversed(range(self.degree())):
            print(self.items[i], end='')
            if i != 0:
                print("x^%d + " % i, end='')
        print("\n")

    def add(self, b):  # 현재 다항식과 다항식b를 더한 새로운 다항식을 만들어 반환
        p = Polynomial()  # 더해진 새로운 다항식을 리턴받을 p선언
        if self.degree() > b.degree():  # 현재 다항식의 차수 > 추가된 b 다항식의 차수
            for i in range(0, self.degree()):  # 0부터 현재다항식의 차수-1까지
                if (i >= b.degree()):  # i가 b다항식의 차수보다 크거나 같다면
                    p.items.append(self.items[i])
                else:
                    p.items.append(self.items[i] + b.items[i])
        else:
            for i in range(0, b.degree()):
                if (i >= self.degree()):
                    p.items.append(b.items[i])
                else:
                    p.items.append(self.items[i] + b.items[i])
        return p

    def eval(self, x):  # 미지수에 x를 넣어 계산한 결과 반환
        result = 0
        for i in range(self.degree()):
            result += self.items[i]*pow(x, i)
        return result

    def read(self):  # 다항식 입력받음
        self.items = list(
            map(float, input("최고차항부터 차수를 순서대로 입력하시오. : ").split(" ")))
        self.items.reverse()


a = Polynomial()
b = Polynomial()
a.read()
b.read()
c = a.add(b)
a.display("   A(x) = ")
b.display("   B(x) = ")
c.display("   A+B  = ")
print("   C(2) =", c.eval(2))
