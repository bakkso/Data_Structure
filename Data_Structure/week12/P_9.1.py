class BSTNode:
    def __init__(self, key, value):
        self.key = key
        self.value = value
        self.left = None
        self.right = None


def search_max_bst_recur(n):
    if n.right == None:
        return n.key
    else:
        return search_max_bst_recur(n.right)


def search_min_bst_recur(n):
    if n.left == None:
        return n.key
    else:
        return search_min_bst_recur(n.left)


# def search_max_bst_recur(n):
#     if n.right is not None:
#         return search_max_bst_recur(n.right)
#     else:
#         return n.key


# def search_min_bst_recur(n):
#     if n.left is not None:
#         return search_min_bst_recur(n.left)
#     else:
#         return n.key

# ------------------------------------------------------------


def count_node(n):
    if n is None:
        return 0
    else:
        return 1 + count_node(n.left) + count_node(n.right)


def insert_bst(r, n):
    if n.key < r.key:
        if r.left is None:
            r.left = n
            return True
        else:
            return insert_bst(r.left, n)
    elif n.key > r.key:
        if r.right is None:
            r.right = n
            return True
        else:
            return insert_bst(r.right, n)
    else:
        return False


def delete_bst_case1(parent, node, root):
    if parent is None:
        root = None
    else:
        if parent.left == node:
            parent.left = None
        else:
            parent.right = None

    return root


def delete_bst_case2(parent, node, root):
    if node.left is not None:
        child = node.left
    else:
        child = node.right

    if node == root:
        root = child
    else:
        if node is parent.left:
            parent.left = child
        else:
            parent.right = child

    return root


def delete_bst_case3(parent, node, root):
    succp = node
    succ = node.right
    while (succ.left != None):
        succp = succ
        succ = succ.left

    if (succp.left == succ):
        succp.left = succ.right
    else:
        succp.right = succ.right

    node.key = succ.key
    node.value = succ.value
    node = succ

    return root


def delete_bst(root, key):
    if root == None:
        return None

    parent = None
    node = root
    while node != None and node.key != key:
        parent = node
        if key < node.key:
            node = node.left
        else:
            node = node.right

    if node == None:
        return None
    if node.left == None and node.right == None:
        root = delete_bst_case1(parent, node, root)
    elif node.left == None or node.right == None:
        root = delete_bst_case2(parent, node, root)
    else:
        root = delete_bst_case3(parent, node, root)


def inorder(n):
    if n is not None:
        inorder(n.left)
        print(n.key, end=' ')
        inorder(n.right)
# ------------------------------------------------------------


class BSTMap():
    def __init__(self):
        self.root = None

    def isEmpty(self): return self.root == None
    def clear(self): self.root = None
    def size(self): return count_node(self.root)

    def findMax(self): return search_max_bst_recur(self.root)
    def findMin(self): return search_min_bst_recur(self.root)

    def insert(self, key, value=None):
        n = BSTNode(key, value)
        if self.isEmpty():
            self.root = n
        else:
            insert_bst(self.root, n)

    def delete(self, key):
        delete_bst(self.root, key)

    def display(self, msg='BSTMap :'):
        print(msg, end='')
        inorder(self.root)
        print()


print("\n======= 이진탐색트리 테스트 ===================================")
map = BSTMap()
data = [35, 18, 7, 26, 12, 3, 68, 22, 30, 99]
print("[삽입 연산] : ", data)

for key in data:
    map.insert(key)

map.display("[중위 순회] : ")

print("최댓값= ", map.findMax())
print("최솟값= ", map.findMin())
