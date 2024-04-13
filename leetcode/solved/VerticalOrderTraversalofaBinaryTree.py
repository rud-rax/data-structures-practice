# from collections import OrderedDict
from collections import defaultdict


class Node:
    def __init__(self, data, left=None, right=None) -> None:
        self.data = data
        self.left = left
        self.right = right


def verticalorderTransversal(root):
    x = 0

    dic = defaultdict(lambda: None)

    def add(x, node):

        if dic[x]:
            dic[x].append(node.data)
        else:
            dic[x] = [node.data]

        if node.left:
            add(x - 1, node.left)
        if node.right:
            add(x + 1, node.right)

    add(x, root)

    print(dic)

    ans = []
    for i in sorted(list(dic.keys())):
        # print(f" {i} {dic[i]}")
        ans.append(dic[i])

    return ans


def solve(root):
    a, b = 0, 0


# def inorderTraversal(root):

#     # node = root
#     queue = [root]
#     visited = []
#     while len(queue):
#         node = queue.pop(0)
#         if node:
#             queue.append(node.left)
#             queue.append(node.right)

#             visited.append(node.data)

#         # else:
#         #     visited.append(None)

#     for i in visited:
#         print(i)


if __name__ == "__main__":

    # tree
    # n = Node(3)
    # n.left = Node(9)
    # n.right = Node(20)
    # n.right.left = Node(15)
    # n.right.right = Node(7)

    n = Node(1)
    n.left = Node(2)
    n.right = Node(3)
    n.left.left = Node(4)
    n.left.right = Node(6)
    n.right.left = Node(5)
    n.right.right = Node(7)

    # inorderTraversal(n)
    print(verticalorderTransversal(n))
