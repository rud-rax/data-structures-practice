n = int(input())

for _ in range(n):

    x, y = list(map(int, input().rstrip().split()))

    if x == y:
        print("ANY")

    elif x > y:
        print("SECOND")

    elif x < y:
        print("FIRST")
