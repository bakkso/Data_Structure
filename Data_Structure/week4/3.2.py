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

# delete() 함수와 replace() 함수는 이전 버전에서 삭제된 내용이므로 삭제합니다.
"""
    def delete(pos):
        return A.pop(pos)

    def replace(pos, elem):
        A[pos] = elem
    """
