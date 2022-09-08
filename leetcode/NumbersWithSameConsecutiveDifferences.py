# method 1
def solve1(n, k):

    arr = []

    def make(num, n, k):
        if n > 0:
            a = num % 10
            no = num

            if 0 <= a - k <= 9:
                no = num * 10
                no += a - k
                if n - 1 == 1 and no not in arr:
                    arr.append(no)
                else:
                    make(no, n - 1, k)

            no = num

            if 0 <= a + k <= 9:
                no = num * 10
                no += a + k
                if n - 1 == 1 and no not in arr:
                    arr.append(no)
                else:
                    make(no, n - 1, k)

    N, K = 2, 1
    for i in range(1, 10):
        make(i, N, K)

    print(arr)


# method 2


def solve2(n, k):

    if n == 1:
        return [i for i in range(10)]

    ans = []

    def dfs(n, num):

        if n == 0:
            return ans.append(num)

        queue = set([num % 10 - k, num % 10 + k])

        for j in queue:
            if 0 <= j <= 9:
                dfs(n - 1, num * 10 + j)

    for i in range(1, 10):
        dfs(n - 1, i)

    return ans


if __name__ == "__main__":
    n, k = 3, 7

    print(solve2(n, k))
