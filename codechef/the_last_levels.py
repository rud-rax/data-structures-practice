n = int(input())


for _ in range(1):
    x, y, z = list(map(int, input().rstrip().split()))

    ans = x * y + (((x - 1) // 3) * z)
    print(ans)
