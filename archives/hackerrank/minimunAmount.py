arr = [1, 5, 3]


def solve(arr):
    def partition(l, h):
        pivot = arr[l]
        i = l
        j = h

        while i < j:
            while pivot >= arr[i] and i < j:
                i += 1
            while pivot < arr[j]:
                j -= 1
            if i < j:
                arr[i], arr[j] = arr[j], arr[i]

        arr[j], arr[l] = arr[l], arr[j]
        return j

    def quickSort(l, h):
        if l < h:
            x = partition(l, h)
            quickSort(l, x)
            quickSort(x + 1, h)

    quickSort(0, len(arr) - 1)

    return arr


print(solve(arr))
