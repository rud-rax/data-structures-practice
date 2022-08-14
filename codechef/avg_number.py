t = int(input())

for i in range(t):
    n, k, v = list(map(int, input().rstrip().split()))
    arr = list(map(int, input().rstrip().split()))

    x = v * (n + k) - sum(arr)

    num = x / k

    if x % k != 0:
        print(-1)

    elif num < 0:
        print(-1)
    else:
        print(int(num))

        
