import math


class AprioriAlgo:
    def __init__(self, n=10, table=[], min_support=30):
        self.n = n
        self.table = table
        self.freqtable = {}
        self.setfreqtable = {}
        self.min_support = math.ceil(min_support * self.n / 100)

    def createTable(self):

        for i in range(1, self.n + 1):
            inp = input(f"Enter the {i} transaction --> ")
            inp.lower()
            t = []
            for word in inp.split():
                t.append(word)
            self.table.append(t)

    def getTable(self):

        for row in self.table:
            for col in row:
                print(f"{col}", end=" ")
            print()
        return self.table

    def getFreqTable(self):
        for k in self.freqtable:
            print(k, self.freqtable[k])

    def combinationItems(self, i):

        combList = []
        ll = list(self.setfreqtable[i])

        for i in range(len(ll)):
            j = i + 1
            while j < len(ll):

                combList.append([ll[i], ll[j]])
                j += 1

        # print(combList)
        return combList

    def checkItems(self, ll):

        C = 0
        for row in self.table:
            cc
            for item in ll:
                if item in row:
                    cc += 1

            if cc == len(ll):
                c += 1
        print(c)
        return c

    def solveFor(self, i):

        self.freqtable[i] = {}
        self.setfreqtable[i] = {}

        for row in self.table:
            for col in row:
                if col in self.freqtable[i].keys():
                    self.freqtable[i][col] += 1
                else:
                    self.freqtable[i][col] = 1

        for item in self.freqtable[i]:
            if self.freqtable[i][item] >= self.min_support:
                self.setfreqtable[i][item] = self.freqtable[i][item]

    # def solve(self) :
    #     i = 0

    #     while i < 3 :

    #         self.solveFor(i)
    #         self.combinationItems(i)

    #         self.freqtable[]

    #         i += 1


table = [
    ["milk", "egg", "bread", "butter"],
    ["milk", "butter", "egg", "ketchup"],
    ["bread", "butter", "ketchup"],
    ["milk", "bread", "butter"],
    ["bread", "butter", "cookie"],
    ["milk", "bread", "butter", "cookie"],
    ["milk", "cookie"],
    ["milk", "bread", "butter"],
    ["bread", "butter", "egg", "cookie"],
    ["milk", "butter", "bread"],
    ["milk", "bread", "butter"],
    ["milk", "bread", "cookie", "ketchup"],
]


if __name__ == "__main__":

    ap = AprioriAlgo(12, table)

    # ap.createTable()
    # ap.getTable()
    print(ap.freqtable)
    ap.solveFor(1)
    ap.getFreqTable()
    print(ap.min_support)

    print(ap.setfreqtable)

    ap.combinationItems(1)
