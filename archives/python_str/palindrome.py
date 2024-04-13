
def checkPalindrome(st):

    l = 0
    r = len(st) - 1

    while l < r:
        if st[l] != st[r]:
            return False

        l += 1
        r -= 1

    return True


print(checkPalindrome("geek"))
print(checkPalindrome("maam"))
print(checkPalindrome("madam"))
print(checkPalindrome("eye"))
