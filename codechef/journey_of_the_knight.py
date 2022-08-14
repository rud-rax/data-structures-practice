# cook your dish here


def findNext(i, j, now):

    if 1 <= i - 1 <= 8 and 1 <= j - 2 <= 8 and [i - 1, j - 2] not in now:
        now.append([i - 1, j - 2])

    if 1 <= i + 1 <= 8 and 1 <= j - 2 <= 8 and [i + 1, j - 2] not in now:
        now.append([i + 1, j - 2])

    if 1 <= i - 2 <= 8 and 1 <= j - 1 <= 8 and [i - 2, j - 1] not in now:
        now.append([i - 2, j - 1])

    if 1 <= i - 2 <= 8 and 1 <= j + 1 <= 8 and [i - 2, j + 1] not in now:
        now.append([i - 2, j + 1])

    if 1 <= i - 1 <= 8 and 1 <= j + 2 <= 8 and [i - 1, j + 2] not in now:
        now.append([i - 1, j + 2])

    if 1 <= i + 1 <= 8 and 1 <= j + 2 <= 8 and [i + 1, j + 2] not in now:
        now.append([i + 1, j + 2])

    if 1 <= i + 2 <= 8 and 1 <= j + 1 <= 8 and [i + 2, j + 1] not in now:
        now.append([i + 2, j + 1])

    if 1 <= i + 2 <= 8 and 1 <= j - 1 <= 8 and [i + 2, j - 1] not in now:
        now.append([i + 2, j - 1])

    return now


# findNext(8,2)
# 8 8 8 6 y


def solve():
    x1, y1, x2, y2 = list(map(int, input().rstrip().split()))

    now = [[x1, y1]]
    next = []

    for _ in range(100):
        for x, y in now:
            next = findNext(x, y, next)
        print(now)

        now = next
        next = []

    print("PRESENT - > ", now)

    if [x2, y2] in now:
        print("YES")
    else:
        print("NO")


t = 1
# t = int(input())

for _ in range(t):
    solve()
