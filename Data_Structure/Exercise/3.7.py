def same(A,B):
    for i in A:
        if i in B:
            return True
    return False #return이 한 번 더 들여쓰지 않도록 주의 (들여쓰기를 한 번 더 하면 다른 실행결과가 됨)

A = list(map(int, input().split()))
B = list(map(int, input().split()))
print(same(A,B))
