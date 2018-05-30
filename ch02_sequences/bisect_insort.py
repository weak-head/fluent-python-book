#!/python/bin

import bisect

HAYSTACK = [1, 4, 5, 6, 8, 12, 15, 20, 21, 23, 23, 26, 29, 30]
NEEDLES  = [0, 1, 2, 5, 8, 10, 22, 23, 29, 30, 31]

ROW_FORMAT = '{0:2d} @ {1:2d}    {2}{0:<2d}'


def bisect_demo(bisect_fn):
    '''
    visualizing the way how bisect works
    '''

    for needle in reversed(NEEDLES):
        index = bisect_fn(HAYSTACK, needle)
        offset = '  |' * index
        print(ROW_FORMAT.format(needle, index, offset))


if __name__ == '__main__':

    print('bisect right:')
    print('haystack ->', ' '.join('%2d' % n for n in HAYSTACK))
    bisect_demo(bisect.bisect) # bisect_right

    print(); print()
    print('bisect left:')
    print('haystack ->', ' '.join('%2d' % n for n in HAYSTACK))
    bisect_demo(bisect.bisect_left)