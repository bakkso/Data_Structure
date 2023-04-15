class Polynomial:
    def __init__(self):
        self.items = []

    def degree(self):
        return len(self.items)

    def display(self, msg="f(x) = "):
        print(msg, end='')
        for i in reversed(range(self.degree())):
            print(self.items[i], end='')
            if i != 0:
                print("x^%d + " % i, end='')
        print("\n")

    def add(self, b):  # 자기 자신(self)에 b를 더해라.
        p = Polynomial()
        if self.degree() > b.degree():
            for i in range(0, self.degree()):
                if (i >= b.degree()):
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

    def eval(self, x):
        result = 0
        for i in range(self.degree()):
            result += self.items[i]*pow(x, i)
        return result

    def read(self):
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
