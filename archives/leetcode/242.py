from collections import defaultdict


def solve(s,t) : 
    d = defaultdict(lambda : 0)

    for l in s :
        d[l] += 1

    for l in t :
        d[l]-=1

    for k in d.keys() :
        if k :
            return False
    return True


if __name__ == "__main__" :
    print(solve(s = "anagram", t = "nagaram"))