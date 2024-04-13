def left_rotate(l, shift=1):

    for i in range(shift):
        ele = l.pop(0)
        l.append(ele)
    print(l)
    return l


def left_rotate_slicing(l, shift=1):

    l = l[shift:] + l[:shift]
    print(l)
    return l


def right_rotate_slicing(l, shift=1):
    # shift = len(l) - shift
    # l = l[shift:] + l[:shift]

    l = l[-shift:] + l[:-shift]

    print(l)
    return l


if __name__ == "__main__":
    list = [10, 20, 30, 40]

    # left_rotate(list, 2)
    # left_rotate_slicing(list, 2)
    right_rotate_slicing(list, 2)
