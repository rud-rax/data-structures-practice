# arr = [10, 5, 8, 9, 3, 6, 15, 12, 16]
arr = [14, 12, 70, 15, 95, 65, 22, 30]


# def partition(l, h):

#     pivot = arr[l]

#     i = l
#     j = h

#     while i < j:

#         while arr[i] <= pivot:
#             i += 1
#         while arr[j] > pivot:
#             j -= 1

#         if i < j:
#             arr[i], arr[j] = arr[j], arr[i]
#             print(arr)

#     arr[l], arr[j] = arr[j], arr[l]

#     return j


# def quick_sort(l, h):
#     if l < h:
#         j = partition(l, h)

#         quick_sort(l, j)
#         quick_sort(j + 1, h)


def partition(l, h):

    pivot = arr[l]
    i = l
    j = h

    while arr[i] <= pivot and i < j:
        i += 1
    while arr[j] > pivot:
        j -= 1

    if i < j:
        arr[i], arr[j] = arr[j], arr[i]

    arr[j], arr[l] = arr[l], arr[j]
    return j


def quick_sort(l, h):

    if l < h:
        x = partition(l, h)

        quick_sort(l, x)

        quick_sort(x + 1, h)


quick_sort(0, len(arr) - 1)
print(arr)
