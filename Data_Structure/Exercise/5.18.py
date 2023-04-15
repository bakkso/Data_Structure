D = [1, 2, 3, 4, 5, 6, 7, 8]
S = []

# D는 덱, S는 스택
# S 스택은 LIFO (Last In First Out)
for i in range(0, 8):
    if not len(D) == 0: # 공백이 아닐때 실행하라 (pop때문에)
        S.append(D.pop(0)) #D의 첫번째 배열부터 S리스트 뒤로 순차적으로 삽입함


# (start, step, stop) S 리스트의 마지막 인덱스부터 0번째 배열까지 역순으로 반복
#for i in range(len(S)-1, -1, -1): # 조교'advice : pop(i)는 항상 pop(-1)이 될테니까 인덱싱을 할 필요는 없다
for i in range(0,8):
    if not len(S) == 0:  # 공백이 아닐때 실행하라 (pop때문에)
        D.append(S.pop())  # S는 LIFO이므로 마지막으로 들어온 요소부터 out 해줘야됨
        print(i)
        print("D   덱 : ", D)
        print("S 스택 : ", S)
print(D)
 
 