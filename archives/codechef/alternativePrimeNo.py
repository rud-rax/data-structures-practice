arr = [1, 4, 3, 7, 10, 2]
arr = [1, 3, 4, 6, 8, 10]
arr = [2, 3, 5, 7, 9]

arr = sorted(arr)
print(arr)


def isPrime(n):

    if n == 1:
        return False
    i = 2
    while i < n:
        if n % i == 0:
            return False
        i += 1

    return True


j = len(arr) - 1
i = len(arr) - 1
while isPrime(arr[j]) and j >= 0:
    j -= 1

while not isPrime(arr[i]) and i >= 0:
    i -= 1

# print(arr)
# print(i, j)
seq = []
while i >= 0 or j >= 0:

    if len(seq) % 2 == 0:
        if j < 0:
            break
        seq.append(arr[j])
        j -= 1
        print(seq)
        while isPrime(arr[j]) and j >= 0:
            # print(arr[j])
            j -= 1

    else:
        if i < 0:
            break
        seq.append(arr[i])
        i -= 1
        print(seq)
        while not isPrime(arr[i]) and i >= 0:
            # print(arr[i])
            i -= 1


print(sum(arr) - sum(seq))
