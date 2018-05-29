
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


def stride_example():
    '''
    Strides could be used to specify a step
    that is used to slice items from the
    sequence
    '''

    some_sequence = 'the sequence to be sliced'

    r = some_sequence[::2]  # gets every seconds character
    print(r)

    r = some_sequence[::-1]  # every character in opposite order
    print(r)

    r = some_sequence[::-2]  # every seconds character in opposite order
    print(r)


def stride_for_nice_slicing():
    '''
    strides could be used for pretty nice
    slicing or well structured data
    '''

    well_structured_data = """
    0.........10...15........25....
    John      M    $15.75    34
    Doe       M    $337.25   18
    Alice     W    $3.15     372
    Dona      W    $0.75     91
    """

    NAME = slice(0, 10)
    SEX = slice(10, 15)
    DEBT = slice(15, 25)
    KARMA = slice(25, 30)

    rows = well_structured_data.split('\n')[2:]

    for record in rows:
        print('{name:10} - {debt:6}'.format(name=record[NAME], debt=record[DEBT]))


def assigning_to_slices():
    '''
    slices could be used with an 
    assignment statement or del statement
    '''

    l = list(range(10))
    print(l)
    
    l[2:5] = [20, 30]
    print(l)

    del l[5:7]
    print(l)

    l[3::2] = [11, 22]
    print(l)

    try:
        l[2:5] = 100
    except:
        print('only sequences could be used during assignment')

    l[2:5] = [100]
    print(l)



if __name__ == '__main__':

    exclude_last_item()

    stride_example()

    stride_for_nice_slicing()

    assigning_to_slices()