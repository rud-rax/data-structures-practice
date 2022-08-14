M = 7


class MyHash:
    def __init__(self, m=7):

        self.EMPTYSYM = "EMP"
        self.DELETESYM = "DEL"
        self.table = [self.EMPTYSYM for _ in range(m)]
        self.m = m

    def function(self, e, i):

        return ((e % self.m) + i) % self.m

    def insert(self, e):
        print(f"INSERT {e}")

        i = 0
        while i < self.m:
            hash = self.function(e, i)
            if self.table[hash] == self.EMPTYSYM or self.table[hash] == self.DELETESYM:
                self.table[hash] = e
                break
            i += 1

    def delete(self, e):

        print(f"DELETE {e}")

        i = 0
        while i < self.m:
            hash = self.function(e, i)
            if self.table[hash] == e:
                self.table[hash] = self.DELETESYM
                break
            i += 1

    def search(self, e):
        print(f"SEARCH {e}", end=" ")

        i = 0
        while i < self.m:
            hash = self.function(e, i)
            if self.table[hash] == e:
                return True
            elif self.table[hash] == "EMP":
                return False

            i += 1

        return False


if __name__ == "__main__":

    ht = MyHash(M)

    ht.insert(50)
    ht.insert(51)
    ht.insert(15)
    ht.insert(56)
    ht.insert(72)

    print(ht.table)

    print(ht.search(56))

    ht.delete(56)
    print(ht.search(56))
    print(ht.table)

    ht.insert(54)
    print(ht.table)
