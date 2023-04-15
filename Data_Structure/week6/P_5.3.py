from circularQueue import CircularQueue


def fibo(n):
    Q = CircularQueue()

    if (n <= 1):
        return n
    else:
        Q.enqueue(0)
        Q.enqueue(1)
        for i in range(2, n+1):

            A: int = Q.dequeue()

            B: int = Q.peek()

            val = A + B

            Q.enqueue(val)

        return val


for i in range(0, 10):
    print("F(%d) = " % i, fibo(i))
