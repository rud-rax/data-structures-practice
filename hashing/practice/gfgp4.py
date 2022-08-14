# arr = list({1, 2, 3, 4, 5, 6, 7, 8, 9, 10})
arr = list({2, 5})

sum = 10

print(arr)


def findPair(arr, sum):

    hashmap = {}
    c = 0
    for ele in arr:
        temp = sum - ele
        # print(temp)
        if temp in arr and temp != ele and temp not in hashmap.keys():
            print(f"ANS -> {ele} , {temp}")
            hashmap[ele] = temp
            # return 1
            # break
            c += 1

    # print(hashmap.keys())
    return c


print(findPair(arr, sum))
