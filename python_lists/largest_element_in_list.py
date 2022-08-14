def largest_element_in_list(l):
    if not l:
        return None
    max_ele = l[0]

    for ele in l[1:]:
        if max_ele < ele:
            max_ele = ele

    print(max_ele)
    return max_ele


def second_largest_element(l):

    if not l:
        return None

    else:

        me1 = largest_element_in_list(l)
        for i in l:
            if i == me1:
                l.remove(me1)

        me2 = largest_element_in_list(l)

        return me2


def n_largest_element(l, n):
    if not l:
        return None

    for _ in range(n - 1):
        me1 = largest_element_in_list(l)
        for i in l:
            if i == me1:
                l.remove(me1)

    me = largest_element_in_list(l)

    return me


def optimized_second_largest(ll):

    if not ll:
        return None

    # sl, l = min([ll[0], ll[1]]), max([ll[0], ll[1]])

    sl = None
    l = ll[0]

    # i = 0
    # while sl == l and i < len(l):
    #     sl, l = min([ll[0], ll[i]]), max([ll[0], ll[i]])
    # else:
    #     if sl == l :
    #         return None

    for x in ll:

        if x < l:
            if sl < x or sl == None:
                sl = x

        elif x > l:
            l, sl = x, l

    print(sl)
    return sl


# l = [10, 70, 30, 60, 90, 20, 40]
l = [10, 10, 10, 10]
# largest_element_in_list(l)
# second_largest_element(l)
# n_largest_element(l, 4)
optimized_second_largest(l)
