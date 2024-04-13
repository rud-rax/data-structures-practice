def bubblesort(arr):

    for i in range(len(arr) - 1):
        isSort = True
        for j in range(len(arr) - i - 1):
            if arr[j] > arr[j + 1]:
                isSort = False
                arr[j], arr[j + 1] = arr[j + 1], arr[j]

        if isSort == True:
            break

    return arr


# arr = [8, 10, 2, 7]
arr = [4, 9, 13, 15, 1, 6]


print(bubblesort(arr))
