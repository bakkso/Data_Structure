def sum(n):
    if n == 1:
        return 1
    else:
        return n + sum(n-1)


n = int(input("숫자를 입력하세요 : "))
print(sum(n))
