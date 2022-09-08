class Node:
    def __init__(self, data, left=None, right=None) -> None:
        self.data = data
        self.left = left
        self.right = right


def inorderTraversal(root):

    # node = root
    queue = [root]
    visited = []
    while len(queue):
        node = queue.pop(0)
        if node:
            queue.append(node.left)
            queue.append(node.right)

            visited.append(node.data)

        else:
            visited.append(None)

    for i in visited:
        print(i)


def solve(arr):
    root = None
    for par, chl, isl in arr:
        if not root:
            root = Node(par)
            if isl:
                root.left = Node(chl)
            else:
                root.right = Node(chl)

        elif root.data == par:
            if isl:
                root.left = Node(chl)
            else:
                root.right = Node(chl)

        else:
            node = Node(par)
            if chl == root.data:
                if isl:
                    node.left = root
                else:
                    node.right = root
                root = node

    return root


if __name__ == "__main__":
    test = [[20, 15, 1], [20, 17, 0], [50, 20, 1], [50, 80, 0], [80, 19, 1]]
    test1 = [[1, 2, 1], [2, 3, 0], [3, 4, 1]]
    inorderTraversal(solve(test1))
