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
        try:
            self.preorder(2*n)
        except:
            pass
        try:
            self.preorder(2*n+1)
        except:
            pass

    def inorder(self, n):
        if self.tree[n] == None:
            return
        try:
            self.inorder(2*n)
        except:
            pass
        print(self.tree[n], end='')
        try:
            self.inorder(2*n+1)
        except:
            pass

    def postorder(self, n):
        if self.tree[n] == None:
            return
        try:
            self.postorder(2*n)
        except:
            pass
        try:
            self.postorder(2*n+1)
        except:
            pass
        print(self.tree[n], end='')


tree = BinaryTree()

tree.tree = ['', '+', '*', 'E', '*', 'D', '', '', '/', 'C', '', '', '', '',
             '', '', 'A', 'B', '', '', '', '', '', '', '', '', '', '', '', '', '', '']

tree.printPrefix()
tree.printPostfix()
tree.printInfix()
