arr = [3, 7, 2, 23, -19, 8, 5, -11, 15, 4]
arr = [1,4,7,8,10,3,2,5,6,9]


def solve(arr):
    def partition(l, h):

        i = l

        for j in range(l + 1, h + 1):
            if arr[j] < arr[l]:
                i += 1
                arr[i], arr[j] = arr[j], arr[i]

        if i > l:
            arr[i], arr[l] = arr[l], arr[i]

        return i

    def quickSort(l, h):

        if l < h:
            x = partition(l, h)
            quickSort(l, x - 1)
            quickSort(x + 1, h)

    quickSort(0, len(arr) - 1)
    print(arr)

    if (arr[0] * arr[1]) > (arr[-2] * arr[-3]):
        return arr[0] * arr[1] * arr[-1]
    else:
        return arr[-3] * arr[-2] * arr[-1]


print(solve(arr))
# print(arr)
