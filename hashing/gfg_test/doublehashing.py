class HashTable:
    def __init__(self, m):
        self.m = m
        self.EMPTYSYM = "EMP"
        self.DELETESYM = "DEL"

        self.table = [self.EMPTYSYM for _ in range(m)]

    def h1(self, key):
        return key % self.m

    def h2(self, key):
        t = self.m - 1
        return t - (key % t)

    def hashf(self, key, i):
        return (self.h1(key) + i * self.h2(key)) % self.m

    def insert(self, e):

        print(f"INSERT {e}")

        i = 0
        while i < self.m:
            hash = self.hashf(e, i)
            if self.table[hash] == self.EMPTYSYM or self.table[hash] == self.DELETESYM:
                self.table[hash] = e
                break
            i += 1

    def delete(self, e):
        print(f"DELETE {e}")

        i = 0
        while i < self.m:
            hash = self.hashf(e, i)

            if self.table[hash] == e:
                self.table[hash] = self.DELETESYM
                break
            i += 1

    def search(self, e):
        print(f"SEARCH {e}", end=" ")

        i = 0
        while i < self.m:
            hash = self.hashf(e, i)
            # print(self.table[hash])
            if self.table[hash] == e:
                return True

            i += 1

        return False


if __name__ == "__main__":

    ht = HashTable(7)
    ht.insert(49)
    ht.insert(63)
    ht.insert(56)
    ht.insert(52)
    ht.insert(54)
    ht.insert(48)

    print(ht.table)

    print(ht.search(56))

    ht.delete(56)
    print(ht.table)

    print(ht.search(56))
    print(ht.table)

    ht.insert(53)
    print(ht.table)
