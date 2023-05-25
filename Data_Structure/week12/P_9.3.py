from BSTMap import *
from circularQueue import CircularQueue


class BSTNode:
    def __init__(self, key, value):
        self.key = key
        self.value = value
        self.left = None
        self.right = None


class AVLMap(BSTMap):
    def __init__(self):
        super().__init__()

    # def insert(self, key, value=None):
    #     if search_bst(self.root, key) is None:
    #         n = BSTNode(key, value)
    #         if self.isEmpty():
    #             self.root = n
    #         else:
    #             self.root = insert_avl(self.root, n)

    # def insert(self, data):
    #     key, value = data
    #     print("Key : ", key)
    #     print("Value : ", value)
    #     if search_bst(self.root, key) is None:
    #         n = BSTNode(key, value)
    #         if self.isEmpty():
    #             self.root = n
    #         else:
    #             self.root = insert_avl(self.root, n)

    def insert(self, data):
        key, value = data
        n = BSTNode(key, value)
        if self.isEmpty():
            self.root = n
        else:
            self.root = insert_avl(self.root, n)

    # def insert(self, data):
    #     key, value = data
    #     if search_bst(self.root, key) is None:
    #         n = BSTNode(key, value)
    #         if self.isEmpty():
    #             self.root = n
    #         else:
    #             self.root = insert_avl(self.root, n)

    def display(self, msg=''):
        print(msg, end='')
        inorder(self.root)
        print()

# ------------------------------------------------------


def rotateLL(A):
    B = A.left
    A.left = B.right
    B.right = A
    return B


def rotateRR(A):
    B = A.right
    A.right = B.left
    B.left = A
    return B


def rotateRL(A):
    B = A.right
    A.right = rotateLL(B)
    return rotateRR(A)


def rotateLR(A):
    B = A.left
    A.left = rotateRR(B)
    return rotateLL(A)


def reBalance(parent):
    hDiff = calc_height_diff(parent)

    if hDiff > 1:
        if calc_height_diff(parent.left) > 0:
            parent = rotateLL(parent)
        else:
            parent = rotateLR(parent)
    elif hDiff < -1:
        if calc_height_diff(parent.right) < 0:
            parent = rotateRR(parent)
        else:
            parent = rotateRL(parent)
    return parent


def calc_height_diff(n):
    if n == None:
        return 0
    return calc_height(n.left) - calc_height(n.right)


def insert_avl(parent, node):
    if node.key < parent.key:
        if parent.left != None:
            parent.left = insert_avl(parent.left, node)
        else:
            parent.left = node
        return reBalance(parent)

    elif node.key > parent.key:
        if parent.right != None:
            parent.right = insert_avl(parent.right, node)
        else:
            parent.right = node
        return reBalance(parent)
    else:
        print("중복된 키 에러")


def inorder(root):
    if root == None:
        return

    queue = []
    current = root

    while True:
        if current != None:
            queue.append(current)
            current = current.left

        elif queue:
            current = queue.pop()
            if current.key not in queue:
                print([current.key, current.value], end=' ')
            current = current.right
        else:
            break


# ------------------------------------------------------


def count_node(n):
    if n is None:
        return 0
    else:
        return 1 + count_node(n.left) + count_node(n.right)


def count_leaf(n):
    if n is None:
        return 0
    elif n.left is None and n.right is None:
        return 1
    else:
        return count_leaf(n.left) + count_leaf(n.right)


def calc_height(n):
    if n is None:
        return 0
    hLeft = calc_height(n.left)
    hRight = calc_height(n.right)
    if (hLeft > hRight):
        return hLeft + 1
    else:
        return hRight + 1
# ------------------------------------------------------


# node = [7, 8, 9, 2, 1, 5, 3, 6, 4]
# map = AVLMap()

# for i in node:
#     map.insert(i)
#     map.display("AVL(%d): " % i)

# print(" 노드의 개수 = %d" % count_node(map.root))
# print(" 단말의 개수 = %d" % count_leaf(map.root))
# print(" 트리의 높이 = %d" % calc_height(map.root))

# if map.search(5) != None:
#     print('[탐색 5] : 성공')
# else:
#     print('[탐색 5] : 실패')

map = AVLMap()
data = [(11, 'G'), (3, 'C'), (4, 'D'), (1, 'A'), (56, 'J'), (5, 'E'), (6, 'F'),
        (2, 'B'), (98, 'K'), (32, 'H'), (32, 'I')]

print("[삽입 연산] : ", data)

# for node in data:
#     map.insert(node[0], node[1])

for node in data:
    map.insert(node)
map.display("[정렬 결과] : ")
