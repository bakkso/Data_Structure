class BinaryTree:
    def __init__(self, M=32):
        self.tree = [None] * M

    def printPrefix(self, msg='Prefix : '):
        print(msg, end='')
        self.preorder(1)
        print()

    def printPostfix(self, msg='Postfix : '):
        print(msg, end='')
        self.postorder(1)
        print()

    def printInfix(self, msg='Infix : '):
        print(msg, end='')
        self.inorder(1)
        print()

    def preorder(self, n):
        if self.tree[n] == None:
            return
        print(self.tree[n], end='')
        if 2*n < len(self.tree) and self.tree[2*n] is not None:
            self.preorder(2*n)
        if 2*n+1 < len(self.tree) and self.tree[2*n+1] is not None:
            self.preorder(2*n+1)

    def inorder(self, n):
        if self.tree[n] == None:
            return
        if 2*n < len(self.tree) and self.tree[2*n] is not None:
            self.inorder(2*n)
        print(self.tree[n], end='')
        if 2*n+1 < len(self.tree) and self.tree[2*n+1] is not None:
            self.inorder(2*n+1)

    def postorder(self, n):
        if self.tree[n] == None:
            return
        if 2*n < len(self.tree) and self.tree[2*n] is not None:
            self.postorder(2*n)
        if 2*n+1 < len(self.tree) and self.tree[2*n+1] is not None:
            self.postorder(2*n+1)
        print(self.tree[n], end='')


tree = BinaryTree(32)

tree.tree = ['', '+', '*', 'E', '*', 'D', '', '', '/', 'C', '', '', '', '',
             '', '', 'A', 'B', '', '', '', '', '', '', '', '', '', '', '', '', '', '']


tree.printPrefix()
tree.printPostfix()
tree.printInfix()
