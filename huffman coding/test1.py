import huffman_coding as hf


class Test1:
    def __init__(self, t=1):

        self.obj = hf.HuffmanCoding()

        self.t = t

        self.runTest()

    def menu(self) -> None:

        print(
            """
            1 count frequency
            2 make tree
            3 print tree
        """
        )

    def test1(self) -> None:

        self.obj.setMsg("BCCDACCBDABCCDEAAEDA")
        ans = self.obj.countFrequency()
        print(ans)

    def test2(self):
        self.obj.setMsg("BCCDACCBDABCCDEAAEDA")
        self.obj.encode()

    def test3(self):
        # self.obj.setMsg()
        print("ENCODING")
        self.obj.encode("BCCDACCBDABCCDEAAEDA")
        cip1 = self.obj.cip
        print(cip1)

        print("\n\nDECODING")
        t2 = hf.HuffmanCoding(self.obj.tree, self.obj.table)
        print(t2.tree)
        print(t2.table)

        print(t2.decode(cip1))

    def test4(self):
        self.obj.decode("001111101101111001011000111110100010100000110")
        print(self.obj.msg)

    def runTest(self):

        if self.t == 0:
            self.menu()
        elif self.t == 1:
            self.test1()
        elif self.t == 2:
            self.test2()
        elif self.t == 3:
            self.test3()
        elif self.t == 4:
            self.test4()


if __name__ == "__main__":
    t = Test1(3)

    # node = hf.LeafNode("e", 8)
    # print(node.type)

    # node = hf.MidNode(3, 2, 4)
    # print(node.type)
