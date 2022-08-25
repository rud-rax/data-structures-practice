# def partition(l, h):

#     i = l

#     for j in range(l + 1, h + 1):
#         if arr[j] < arr[l]:
#             i += 1
#             arr[i], arr[j] = arr[j], arr[i]

#     arr[i], arr[l] = arr[l], arr[i]

#     return i


# def quickSort(l, h):

#     if l < h:
#         x = partition(l, h)
#         quickSort(l, x - 1)
#         quickSort(x + 1, h)


def partition(l, h):

    i = l

    for j in range(l + 1, h + 1):
        if arr[j] < arr[l]:
            i += 1
            arr[i], arr[j] = arr[j], arr[i]

    arr[i], arr[l] = arr[l], arr[i]

    return i


def quicksort(l, h):
    if l < h:
        x = partition(l, h)
        quicksort(l, x - 1)
        quicksort(x + 1, h)


if __name__ == "__main__":
    arr = [2, 4, 7, 8, 10, 3, 1, 5, 6, 9]
    quicksort(0, len(arr) - 1)
    print(arr)
