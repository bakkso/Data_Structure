import time
import matplotlib.pyplot as plt

# 거듭제곱 순환 함수


def power(x, n):
    if n == 0:
        return 1
    elif (n % 2) == 0:
        return power(x*x, n//2)
    else:
        return x * power(x*x, (n-1)//2)

# 거듭제곱 반복 함수


def power_iter(x, n):
    result = 1.0
    for i in range(n):
        result = result * x
    return result


# 시간 측정
max_n = 2000
step = 100
result_recur = []
for n in range(0, max_n, step):
    start = time.time()
    for i in range(1000):
        answer = power(2, n)
    end = time.time()
    result_recur.append((end-start)*1000)
print("순환: ", result_recur)

result_iter = []
for n in range(0, max_n, step):
    start = time.time()
    for i in range(1000):
        answer = power_iter(2, n)
    end = time.time()
    result_iter.append((end-start)*1000)
print("반복: ", result_iter)

plt.figure()
plt.plot(result_recur[:], label="Recursion")
plt.plot(result_iter[:], label="Iteration")
plt.xlabel('[Nx100]')
plt.ylabel('[Milliseconds]')
plt.show()
