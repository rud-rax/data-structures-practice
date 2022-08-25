arr = [0, 1, 0, 1, 1, 0, 1, 1]
arr = [0, 1, 0]


# naive solution


def naive(arr):

    cost = 0
    for i in range(len(arr)):

        if arr[i] == 0:
            arr[i] = 1
            cost += 1

            for j in range(len(arr[i + 1 :])):

                if arr[j]:
                    arr[j] = 0
                else:
                    arr[j] = 1

    return cost


def greedy(arr):
    cost = 0

    for i in range(len(arr)):

        if (cost % 2) == arr[i]:
            cost += 1

    return cost


# arr = [0, 1, 0]
arr = [0, 1, 0, 1, 1, 0, 1, 1]

print(naive(arr))


# print(greedy(arr))
