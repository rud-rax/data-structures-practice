class Node:
    def __init__(self, data, left=None, right=None):
        self.data = data
        self.right = right
        self.left = left


class Tree:
    def __init__(self, root=None):
        self.root = root
        self.no_of_nodes = 0
        self.countNodes()

        self.height = self.getheight(self.root)

    def countNodes(self):

        if not self.root:
            return 0

        queue = [self.root]
        c = 0
        while len(queue) > 0:
            c += 1
            x = queue.pop(0)
            if x.left:
                queue.append(x.left)
            if x.right:
                queue.append(x.right)

        self.no_of_nodes = c

    def inorder(self, node):

        if node:
            self.inorder(node.left)
            print(node.data)
            self.inorder(node.right)

    def preorder(self, node):
        if node:
            print(node.data)
            self.preorder(node.left)
            self.preorder(node.right)

    def postorder(self, node):
        if node:
            self.postorder(node.left)
            self.postorder(node.right)
            print(node.data)

    def getheight(self, node):
        if not node:
            return 0

        return max(self.getheight(node.left), self.getheight(node.right)) + 1


if __name__ == "__main__":

    n = Node(10)

    n.left = Node(20)
    n.left.left = Node(40)
    n.left.right = Node(50)

    n.right = Node(30)
    n.right.left = Node(60)

    t = Tree(root=n)
    # print(t.countNodes())
    # t.inorder(t.root)

    # t.preorder(t.root)
    # t.postorder(t.root)

    print(t.height)
