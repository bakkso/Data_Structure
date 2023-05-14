from circularQueue import CircularQueue


class TNode:
    def __init__(self, data, left, right):
        self.data = data
        self.left = left
        self.right = right


def preorder(n):
    if n is not None:
        print(n.data, end=' ')
        preorder(n.left)
        preorder(n.right)


def inorder(n):
    if n is not None:
        inorder(n.left)
        print(n.data, end=' ')
        inorder(n.right)


def postorder(n):
    if n is not None:
        postorder(n.left)
        postorder(n.right)
        print(n.data, end=' ')


def levelorder(root):
    queue = CircularQueue()
    queue.enqueue(root)
    while not queue.isEmpty():
        n = queue.dequeue()
        if n is not None:
            print(n.data, end=' ')
            queue.enqueue(n.left)
            queue.enqueue(n.right)
    print()


class BinaryTree:
    def __init__(self, root=None):
        self.root = root

    def isEmpty(self):
        return self.root == None

    def clear(self):
        self.root = None

    def printInOrder(self, msg=' In-Order : '):
        print(msg, end='')
        inorder(root)
        print()

    def printPreOrder(self, msg=' Pre-Order : '):
        print(msg, end='')
        preorder(root)
        print()

    def printPostOrder(self, msg='Post-Order : '):
        print(msg, end='')
        postorder(root)
        print()

    def printLevelOrder(self, msg='Level-Order : '):
        print(msg, end='')
        levelorder(root)


a = TNode('A', None, None)
b = TNode('B', None, None)
d1 = TNode('/', a, b)
c = TNode('C', None, None)
p1 = TNode('*', d1, c)
d = TNode('D', None, None)
p2 = TNode('*', p1, d)
e = TNode('E', None, None)
root = TNode('+', p2, e)

tree = BinaryTree(root)

tree.printInOrder()
tree.printPreOrder()
tree.printPostOrder()
tree.printLevelOrder()
