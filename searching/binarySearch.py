# ar = [2, 3, 6, 8, 12, 17, 23, 26, 34, 44, 52, 59]
k = 23

ar = [2, 3, 6, 17, 23, 33]
# k = 23


def binarySearch(arr, k):
    def bs(l, h):
        if l <= h and l >= 0 and h < len(arr):
            mid = (l + h) // 2
            if arr[mid] == k:
                return mid
            elif arr[mid] < k:
                return bs(mid + 1, h)
            elif arr[mid] > k:
                return bs(l, mid - 1)

    return bs(0, len(arr) - 1)


if __name__ == "__main__":
    print(binarySearch(ar, k))
