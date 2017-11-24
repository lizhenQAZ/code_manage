class Node:
    def __init__(self, elem=-1, lchild=None, rchild=None):
        self.elem = elem
        self.lchild = lchild
        self.rchild = rchild


class Tree:
    def __init__(self, root=None):
        self.root = root

    def add(self, elem):
        node = Node(elem)

        if self.root is None:
            self.root = node
        else:
            queue = []
            queue.append(self.root)
            while queue:
                root_node = queue.pop(0)
                if root_node.lchild is None:
                    root_node.lchild = node
                    return
                if root_node.rchild is None:
                    root_node.rchild = node
                    return
                queue.append(root_node.lchild)
                queue.append(root_node.rchild)

    def preorder(self, root):
        if root is None:
            return
        print(root.elem, end=' ')
        self.preorder(root.lchild)
        self.preorder(root.rchild)

    def preorder_nonrecursive(self, root):
        if root is None:
            return
        self.root = root
        queue = []
        while self.root or queue:
            while self.root:
                print(self.root.elem, end=' ')
                queue.append(self.root)
                self.root = self.root.lchild
            node = queue.pop()
            self.root = node.rchild

    def inorder(self, root):
        if root is None:
            return
        self.inorder(root.lchild)
        print(root.elem, end=' ')
        self.inorder(root.rchild)

    def inorder_nonrecursive(self, root):
        if root is None:
            return
        self.root = root
        queue = []
        while self.root or queue:
            while self.root:
                queue.append(self.root)
                self.root = self.root.lchild
            node = queue.pop()
            print(node.elem, end=" ")
            self.root = node.rchild

    def postorder(self, root):
        if root is None:
            return
        self.postorder(root.lchild)
        self.postorder(root.rchild)
        print(root.elem, end=' ')

    def postorder_nonrecursive(self, root):
        if root is None:
            return
        self.root = root
        queue1 = []
        queue2 = []
        queue1.append(self.root)
        while queue1:
            node = queue1.pop()
            if node.lchild:
                queue1.append(node.lchild)
            if node.rchild:
                queue1.append(node.rchild)
            queue2.append(node)
        while queue2:
            print(queue2.pop().elem, end=" ")

if __name__ == '__main__':
    tree = Tree()
    tree.add(11)
    tree.add(22)
    tree.add(3)
    tree.add(77)
    tree.add(66)
    tree.add(88)  # 11 22 3 77 66 88
    #      11
    #   22    3
    # 77 66 88
    tree.preorder(tree.root)  # 11 22 77 66 3 88
    print(' ')
    tree.inorder(tree.root)  # 77 22 66 11 88 3
    print(' ')
    tree.postorder(tree.root)  # 77 66 22 88 3 11
    print(' ')
    # tree.preorder_nonrecursive(tree.root)  # 11 22 77 66 3 88
    # print(' ')
    # tree.inorder_nonrecursive(tree.root)  # 77 22 66 11 88 3
    # print(' ')
    tree.postorder_nonrecursive(tree.root)  # 77 66 22 88 3 11
    print(' ')
