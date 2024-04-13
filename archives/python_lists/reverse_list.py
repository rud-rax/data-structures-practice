def reverse_list(li):

    l = 0
    r = len(li) - 1

    while l < r:

        print(f"L : {li[l]}  R : {li[r]}")

        li[l], li[r] = li[r], li[l]
        print(f"L : {li[l]}  R : {li[r]}")

        l += 1
        r -= 1

    # print(li)
    return li


l = [10, 20, 30, 60, 40]
print(reverse_list(l))
