from collections import Counter
from unicodedata import name
from xml.dom.minicompat import NodeList




class HuffmanCoding:
    def __init__(self, tree=None, table={}):
        self.msg = ""
        self.cip = ""
        self.tree = tree
        self.table = table

    def getMsg(self):
        return self.msg

    def setMsg(self, msg):
        self.msg = msg

    def encode(self, msg):
        self.setMsg(msg)
        arr = self.countFrequency()

        self.tree = self.makeTree(arr)

        self.makeTable()

        self.cip = ""
        for l in msg:
            self.cip += self.table[l]

        return self.cip

    def decode(self, cip):

        msg = ""

        head = self.tree
        node = head
        i = 0
        while i < len(cip):
            if cip[i] == "0" and node.left:
                node = node.left
                i += 1
            elif cip[i] == "1" and node.right:
                node = node.right
                i += 1
            else:
                msg += node.name
                node = head
        msg += node.name
        self.msg = msg
        return msg

    def countFrequency(self):

        c1 = Counter(self.msg)

        return c1.most_common()[::-1]

    def makeTree(self, arr):

        ht = HuffmanTree(arr)

        ht.build()
        ht.printTreeDFS()

        return ht.head

    def makeTable(self):

        queue = [[self.tree, ""]]
        table = {}

        while len(queue) > 0:
            x = queue.pop(0)
            if x[0].type:
                d = x[1]

                d += "0"
                queue.append([x[0].left, d])

                d = d[:-1]
                d += "1"
                queue.append([x[0].right, d])

            else:

                table[x[0].name] = x[1]

        print(table)

        self.table = table


class HuffmanTree:
    def __init__(self, node_list):

        self.head = None
        self.nodeList = node_list

    def build(self):

        n1 = LeafNode(self.nodeList[0][1], self.nodeList[0][0])
        n2 = LeafNode(self.nodeList[1][1], self.nodeList[1][0])

        self.head = MidNode(0, n1, n2)
        # print(self.head.data)
        self.nodeList.pop(0)
        self.nodeList.pop(0)

        while len(self.nodeList) > 0:
            if len(self.nodeList) == 1:
                n2 = LeafNode(self.nodeList[0][1], self.nodeList[0][0])
                n1 = MidNode(0, self.head, n2)

                self.head = n1

                self.nodeList.pop(0)

            elif self.nodeList[1][1] < self.head.data:
                n2 = LeafNode(self.nodeList[0][1], self.nodeList[0][0])
                n1 = LeafNode(self.nodeList[1][1], self.nodeList[1][0])
                n0 = MidNode(0, n2, n1)
                n = MidNode(0, self.head, n0)

                self.head = n

                self.nodeList.pop(0)
                self.nodeList.pop(0)

            else:
                n2 = LeafNode(self.nodeList[0][1], self.nodeList[0][0])
                n1 = MidNode(0, self.head, n2)

                self.head = n1

                self.nodeList.pop(0)

        # print(self.head.data)
        return self.head

    def printTreeBFS(self):

        stack = [self.head]

        while len(stack) > 0:
            x = stack.pop(0)
            if x.type:
                print(x.data)

                stack.append(x.left)
                stack.append(x.right)

            else:
                print(f"{x.data} {x.name}")

    def printTreeDFS(self):
        queue = [self.head]

        while len(queue) > 0:
            x = queue.pop(0)

            if x.type:
                print(x.data)

                queue.insert(0, x.right)
                queue.insert(0, x.left)

            else:
                print(f"{x.data} {x.name}")


class Node:
    def __init__(self, data) -> None:
        self.data = data


class LeafNode(Node):
    def __init__(self, data, name) -> None:
        super().__init__(data)

        self.left = None
        self.right = None
        self.type = 0
        self.name = name


class MidNode(Node):
    def __init__(self, data, left: Node, right: Node) -> None:
        super().__init__(data)

        self.left = left
        self.right = right
        self.type = 1

        self.data = self.left.data + self.right.data


if __name__ == "__main__":
    msg = "BCCDACCBDABCCDEAAEDA"
    hf = HuffmanCoding()
    hf.setMsg(msg)
    hf.countFrequency()
