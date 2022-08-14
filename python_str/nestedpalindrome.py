def findPalindromes(text):

    anslist = []

    for i in range(len(text)):
        j = i + 1
        while j <= len(text):

            st = text[i:j]
            print(st)
            if st == st[::-1] and len(text[i:j]) > 1:
                anslist.append(text[i:j])

            j += 1

    return anslist


if __name__ == "__main__":
    print(findPalindromes("aabbbaa"))
