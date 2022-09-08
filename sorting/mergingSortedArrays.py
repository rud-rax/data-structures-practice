def mergeSortedArrays(arr1, arr2):
    res = []

    i = 0
    j = 0
    while i < len(arr1) or j < len(arr2):

        if i >= len(arr1):
            res.append(arr2[j])
            j += 1

        elif j >= len(arr2):
            res.append(arr1[i])
            i += 1

        elif arr1[i] < arr2[j]:
            res.append(arr1[i])
            i += 1

        else:
            res.append(arr2[j])
            j += 1

        # print(res)

    # print(i, j)
    # while i < len(arr1):
    #     res.append(arr1[i])
    #     i += 1

    # while j < len(arr2):
    #     res.append(arr2[j])
    #     j += 1

    return res


def mergeSortedArrays2(arr1, arr2):
    res = []

    i = 0
    j = 0

    while i < len(arr1) and j < len(arr2):

        if arr1[i] < arr2[j]:
            res.append(arr1[i])
            i += 1

        else:
            res.append(arr2[j])
            j += 1

    while i < len(arr1):
        res.append(arr1[i])
        i += 1

    while j < len(arr2):
        res.append(arr2[j])
        j += 1

    return res


def merge(arr, low, mid, high):
    i = 0
    j = mid + 1

    res = []
    while i <= mid and j <= high:

        if arr[i] < arr[j]:

            res.append(arr[i])
            i += 1
        else:

            res.append(arr[j])
            j += 1

    while i <= mid:
        res.append(arr[i])
        i += 1

    while j <= high:
        res.append(arr[j])
        j += 1

    return res


if __name__ == "__main__":
    arr1 = [5, 6, 7, 30]
    arr2 = [10, 15, 20]
    # print(mergeSortedArrays2(arr1, arr2))

    # arr = [10, 15, 20, 11, 13]
    # print(merge(arr, 0, 2, len(arr) - 1))

    arr = [5, 8, 12, 14, 7]

    print(merge(arr, 0, 3, len(arr) - 1))
