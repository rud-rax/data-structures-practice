n = int(input())

for _ in range(n):

    l = list(map(int, input().rstrip().split()))

    x = max(l)
    y = min(l)

    print(x - y)
