def is_sorted(li):

    if len(li) <= 1:
        return True

    i = 1
    while i < len(li):
        if li[i - 1] > li[i]:
            return False
        i += 1
    return True


def selection_sort(all_arr):
    i = len(all_arr) - 1
    while i > 0:
        j = 0
        while j < i:
            print(i, j)
            if all_arr[j] > all_arr[j + 1]:

                all_arr[j], all_arr[j + 1] = all_arr[j + 1], all_arr[j]
            j += 1

        i -= 1
    return all_arr


l = [10, 70, 30, 60, 90, 20, 40]
# l = [2, 1]
# l.sort()
print(selection_sort(l))
