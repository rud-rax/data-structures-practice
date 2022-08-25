def solve(n, p):

    while n > 1:
        if n % p == 0:
            print(n)
            n //= p
        else:
            return False

    return True


print(solve(90, 9))
