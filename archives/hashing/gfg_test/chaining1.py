M = 7


class MyHash:
    def __init__(self, m=7):
        self.table = [[] for _ in range(m)]
        self.m = m

    def function(self, e):

        return e % self.m

    def insert(self, e):
        print(f"INSERT {e}")

        hash = self.function(e)
        self.table[hash].append(e)

    def delete(self, e):

        print(f"DELETE {e}")
        hash = self.function(e)
        self.table[hash].remove(e)

    def search(self, e):
        print(f"SEARCH {e}", end=" ")

        hash = self.function(e)

        return e in self.table[hash]


if __name__ == "__main__":

    ht = MyHash(M)

    ht.insert(70)
    ht.insert(71)
    ht.insert(9)
    ht.insert(56)
    ht.insert(72)

    print(ht.table)

    print(ht.search(56))

    ht.delete(56)
    print(ht.search(56))

    print(ht.table)
