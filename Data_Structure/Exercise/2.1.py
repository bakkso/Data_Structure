dan = int(input("구구단 단 입력: "))

for n in range(1, 10, 1):
    print("%2d  X %2d  = " % (dan, n), dan * n)
