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

    def inorder(self, root):
        if root is None:
            return
        self.inorder(root.lchild)
        print(root.elem, end=' ')
        self.inorder(root.rchild)

    def postorder(self, root):
        if root is None:
            return
        self.inorder(root.lchild)
        self.inorder(root.rchild)
        print(root.elem, end=' ')

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
