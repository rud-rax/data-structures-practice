s1 = "listen"
s2 = "sislent"


def anagram(s1, s2):

    # time complexity = O(n * logn)
    if len(s1) == len(s2):
        s1_list = []
        for l in s1:
            s1_list.append(l)

        # print(s1_list)

        for l in s2:
            if l in s1_list:
                s1_list.remove(l)
            else:

                return False

        if len(s1_list) == 0:
            return True
        else:
            return False

    else:
        return False


def improvedAnagram(s1, s2):

    # time complexity = O(n)

    if len(s1) != len(s2):
        return False

    count = [0] * 256

    for i in range(len(s1)):
        count[ord(s1[i])] += 1
        count[ord(s2[i])] -= 1

    for x in count:
        if x != 0:
            return False

    return True


print(improvedAnagram(s1, s2))
