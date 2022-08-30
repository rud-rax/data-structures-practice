def insertionsort(arr):

    for i in range(1, len(arr)):
        for j in range(i):
            if arr[i] < arr[j]:
                arr[i], arr[j] = arr[j], arr[i]

    return arr


if __name__ == "__main__":
    arr = [2, 4, 7, 8, 10, 3, 1, 5, 6, 9]
    print(insertionsort(arr))
