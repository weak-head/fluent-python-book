#!/bin/python

from array import array


def mem_view_example():

    ar = array('h', [-2, -1, 0, 1, 2])

    memv = memoryview(ar)
    print('ar:', ar)
    print('mv:', memv)

    print('len ar:', len(ar))
    print('len mv:', len(memv))

    print('mv[0]:', memv[0])
    print('ar[0]:', ar[0])

    # casting memview to other type

    memv_oct = memv.cast('B')
    print(memv_oct.tolist())

    memv_oct[5] = 4
    print(memv_oct.tolist())

    print('ar:', ar)


if __name__ == '__main__':
    mem_view_example()

    