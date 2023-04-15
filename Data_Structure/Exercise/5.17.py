D = [1, 2, 3, 4, 5, 6, 7, 8]
Q = []

# D는 덱, Q는 큐
# Q는 FIFO(First In First Out)
for i in range(0, 8):
    if not len(D) == 0:  # 공백이 아닐때 실행하라 (pop때문에)
        # D의 첫번째부터 Q에 삽입 (큐는 후단부터 삽입됨) #pop(-1)은 항상 맨 뒤 요소부터 pop하는 의미
        Q.append(D.pop(-1))

# (start, step, stop)
for i in range(0, 8):
    if not len(Q) == 0:  # 공백이 아닐때 실행하라 (pop때문에)
        D.append(Q.pop(0))  # Q는 FIFO이므로 처음 들어온 요소부터 out 해줘야함.
        print(i)
        print("D  덱 : ", D)
        print("Q  큐 : ", Q)

print(D)
