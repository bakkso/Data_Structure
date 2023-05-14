class BinaryTree:
    def __init__(self, M=32):
        self.tree = [None] * M

    def printPrefix(self, msg='Prefix : '):
        print(msg, end='')
        self.preorder(0)
        print()

    def printPostfix(self, msg='Postfix : '):
        print(msg, end='')
        self.postorder(0)
        print()

    def printInfix(self, msg='Infix : '):
        print(msg, end='')
        self.inorder(0)
        print()

    def preorder(self, n):
        if self.tree[n] is None:
            return
        print(self.tree[n], end='')
        if 2*n+1 < len(self.tree):
            self.preorder(2*n+1)
        if 2*n+2 < len(self.tree):
            self.preorder(2*n+2)

    def inorder(self, n):
        if self.tree[n] is None:
            return
        if 2*n+1 < len(self.tree):
            self.inorder(2*n+1)
        print(self.tree[n], end='')
        if 2*n+2 < len(self.tree):
            self.inorder(2*n+2)

    def postorder(self, n):
        if self.tree[n] is None:
            return
        if 2*n < len(self.tree):
            self.postorder(2*n)
        if 2*n+1 < len(self.tree):
            self.postorder(2*n+1)
        print(self.tree[n], end='')


tree = BinaryTree()

tree.tree = [" ", "+", "*", "E", "*", "D", "/", "C", "A", "B"]

tree.printPrefix()
tree.printPostfix()
tree.printInfix()
