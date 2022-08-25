from math import ceil


def solve(k):

    arr = [2, 1, 1]

    i = 1

    while not arr[i] > (arr[i - 1] + arr[i + 1]) / 2:

        arr[i] += 1

    arr.insert(-1, 1)
    i += 1

    while not arr[i] > (arr[i - 1] + arr[i + 1]) / 2:

        arr[i] += 1

    # arr.insert(-1, 1)
    # i += 1

    return arr


print(solve(3))
