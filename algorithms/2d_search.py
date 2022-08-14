# n = int(input('Enter the number to search --> '))


def search(arr, n):

    for row in arr:

        if not row[0] < n < row[-1]:
            continue

        i = 0
        j = len(row) - 1

        while i <= j:
            mid = (i + j) // 2

            if i == j and row[mid] != n:
                break

            print(f"ele : {row[mid]} index : {mid} i : {i} j : {j} ")

            if row[mid] == n:
                return i, j

            elif n < row[mid]:
                j = mid - 1

            elif row[mid] < n:
                i = mid + 1
            print(f"ele : {row[mid]} index : {mid} i : {i} j : {j} ")

    return


if __name__ == "__main__":
    arr = [
        [1, 4, 7, 11, 15],
        [2, 5, 8, 12, 19],
        [3, 6, 9, 16, 22],
        [10, 13, 14, 17, 24],
        [18, 21, 23, 26, 30],
    ]

    ans = search(arr, 17)
    if ans:
        print("FOUND")
