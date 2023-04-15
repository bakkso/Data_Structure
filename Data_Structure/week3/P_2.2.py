import random
answer = random.randint(1, 99)

min = 0
max = 99
for n in range(10):
    guess = int(input("숫자를 입력하세요(범위:%d~%d): " % (min, max)))
    if answer > guess:
        print("아닙니다. 더 큰 숫자입니다!")
        min = guess
    elif answer < guess:
        print("아닙니다. 더 작은 숫자입니다!")
        max = guess
    elif answer == guess:
        print("정답입니다. %d번 만에 맞추셨습니다." % (n+1))
        break
    if n == 9:
        print("10번을 모두 시도하셨습니다.")
print("게임이 끝났습니다.", sep='', end='')
