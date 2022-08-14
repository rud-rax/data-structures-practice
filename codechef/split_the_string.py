# cook your dish here
import math

t = int(input())

for _ in range(t):

    n, k = list(map(int, input().rstrip().split()))
    s = input()

    def findCounts(s):

        n1 = 0
        n0 = 0
        for i in s:

            if int(i) == 1:
                n1 += 1
            else:
                n0 += 1

        return n0, n1

    n0, n1 = findCounts(s)

    # def findAns(s) :
    #     if s == "" :
    #         return 0
    #     n0,n1 = findCounts(s)
    #     return abs(n0 - n1)

    x = abs(n0 - n1)
    print(math.ceil(x / k))
