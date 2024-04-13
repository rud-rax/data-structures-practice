import math


class Node:
    def __init__(self, val) -> None:
        self.val = val
        self.left = None
        self.right = None


root = Node(5)
root.left = Node(1)
root.right = Node(4)
root.right.left = Node(3)
root.right.right = Node(6)


# root = Node(2)
# root.left = Node(1)
# root.right = Node(3)

# root = Node(5)
# root.left = Node(2)
# root.left.left = Node(1)
# root.left.right = Node(4)
# root.left.right.left = Node(3)
# root.right = Node(7)
# root.right.left = Node(6)
# root.right.right = Node(9)


def validBST(root):

    stack = []
    al = -math.inf
    while True:
        if root != None:
            stack.append(root)
            root = root.left
        else:
            if len(stack) == 0:
                break
            x = stack.pop()
            if x.val <= al:
                return False
            al = x.val
            root = x.right

        return True


print(validBST(root))


# def validBST(node, low, high):
#     if not node:
#         return True
#     elif low < node.val < high:
#         return validBST(node.left, low, node.val) and validBST(
#             node.right, node.val, high
#         )
#     else:
#         return False


# print(validBST(root, -99999, 99999))
