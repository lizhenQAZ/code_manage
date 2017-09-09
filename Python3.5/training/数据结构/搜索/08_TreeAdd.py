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
