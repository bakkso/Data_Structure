def delete(pos):
    return A.pop(pos)

def replace(pos, elem):
    A[pos] = elem

def size(A):
    return len(A)

def display(msg='ArrayList:'):
    print(msg, size(A), A)

A = []

A.insert(0, 10)
display()

A.insert(1, 20)
display()

A.insert(0, 30)
display()

A.insert(2, 40)
display()

A.insert(size(A), 50)
display()

A.insert(1, 60)
display()

replace(2, 70)
display()

delete(2)
display()
