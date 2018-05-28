
def exclude_last_item():
    '''
    An example and simple demonstration
    why slices and ranges exclude last item.
    '''

    the_slice = [0, 1, 2, 3, 4, 5, 6][:3]
    the_range = range(3)

    # easy to see the length of the slice or range
    #   both the slice and the range are having 3 items
    #   and we can explicitly see this in the range/slice
    #   declaration
    for item in the_slice:
        print(item)  # 0 1 2

    for item in the_range:
        print(item)  # 0 1 2

    # ease to compute the length of a slice/range
    # when start and stop are given
    the_slice = [0, 1, 2, 3, 4, 5, 6, 7][2:5]  # length = 5 - 2 = 3   (2 3 4)
    the_range = range(2, 5)  # length = 5 - 2 (2 3 4)

    for item in the_slice:
        print(item)

    for item in the_range:
        print(item)

    # very simple to split sequence in two parts
    # without overlapping
    the_sequence = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

    long_head = the_sequence[:4]  # [0, 1, 2, 3]
    the_tail  = the_sequence[4:]  # [4, 5, 6, 7, 8, 9, 10]

    for lh in long_head:
        print('lh -> ', lh)

    for tt in the_tail:
        print('tt -> ', tt)


if __name__ == '__main__':

    exclude_last_item()