

def add_mul_example():
    '''
    * and + could be used with sequences,
    but they have some pitfalls.
    '''

    l = [1, 2, 3]
    print(l * 3)

    print('abc' * 5)


def list_of_lists():
    '''
    generating list of lists.
    usage and pitfalls
    '''

    # list comprehensions is a good way to
    # generate list of lists
    board = [['_'] * 3 for _ in range(3)]
    print(board)

    board[1][2] = 'X'
    print(board)

    print('')

    # but it's pretty easy to make it
    # work in not the way we want
    bad_board = [['_'] * 3] * 3
    print(bad_board)

    bad_board[1][2] = 'X'
    print(bad_board)
    # the problem here is that outer list
    # is made of three references to the same
    # inner list

    # it's pretty much the same as:
    inner_list = ['_'] * 3
    outer_list = []
    for _ in range(3):
        outer_list.append(inner_list)

    # in opposite to:
    outer_list = []
    for _ in range(3):
        inner_list = ['_'] * 3
        outer_list.append(inner_list)


if __name__ == '__main__':
    list_of_lists()