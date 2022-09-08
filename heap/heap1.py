class Heap:
    def __init__(self, arr: list) -> None:

        self.arr = arr

    def getLeft(self, i):
        if (2 * i + 1) < len(self.arr):
            return self.arr[2 * i + 1]
        return None

    def getRight(self, i):
        if (2 * i + 2) < len(self.arr):
            return self.arr[2 * i + 2]
        return None

    def getParent(self, i):
        if i:
            return self.arr[(i - 1) // 2]
        return None

    def insert(self, n):
        i = len(self.arr)
        self.arr.append(n)

        while self.getParent(i) and self.getParent(i) > self.arr[i]:
            self.arr[i], self.arr[(i - 1) // 2] = self.arr[(i - 1) // 2], self.arr[i]
            i = (i - 1) // 2

    def minHeapify(self , i = 0 ):



        while (
            self.getLeft(i)
            and self.getRight(i)
            and self.arr[i] > min(self.getLeft(i), self.getRight(i))
        ):
            rep = None
            if self.getLeft(i) > self.getRight(i):
                rep = 2 * i + 2
            else:
                rep = 2 * i + 1

            self.arr[i], self.arr[rep] = self.arr[rep], self.arr[i]
            i = rep


   
        

if __name__ == "__main__":
    hp = Heap([60, 20, 15, 40, 50, 100, 25, 45])

    # i = 7
    # print(hp.getLeft(i))
    # print(hp.getRight(i))
    # print(hp.getParent(i))

    # print(hp.arr)
    # hp.insert(12)
    # print(hp.arr)
    # hp.insert(9)
    # print(hp.arr)

    print(hp.arr)
    hp.minHeapify()
    print(hp.arr)
