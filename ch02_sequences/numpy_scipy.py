#!/bin/python

import numpy

if __name__ == '__main__':

    a = numpy.arange(12)
    print(a)
    print(type(a))
    print(a.shape)
    print()

    a.shape = 3, 4
    print(a)
    print(a[2])
    print(a[2, 1])
    print(a[:, 1])
    print()

    b = a.transpose()
    print(b)