def selectionsort(arr):

    for i in range(len(arr)):
        min = i
        for j in range(i, len(arr)):
            if arr[min] > arr[j]:
                min = j

        arr[i], arr[min] = arr[min], arr[i]

    return arr


if __name__ == "__main__":
    arr = [2, 4, 7, 8, 10, 3, 1, 5, 6, 9]

    print(selectionsort(arr))
