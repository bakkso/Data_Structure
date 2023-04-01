def same(A,B):
    for i in A:
        if i in B:
            return True
    return False

A = list(map(int, input().split()))
B = list(map(int, input().split()))
print(same(A,B))
