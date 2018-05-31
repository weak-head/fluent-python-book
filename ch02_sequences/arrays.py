#!/bin/python

from array import array
from random import random
from time import time


def mk_rnd_array(array_size):
    '''
    Generates array of random floats.
    '''

    rnd_nums = (random() for i in range(array_size))
    return array('d', rnd_nums)


if __name__ == '__main__':

    t_start = time()
    rar = mk_rnd_array(10**7)
    print('created in %.3f seconds' % (time() - t_start))

    t_start = time()
    with open('array.bin', 'wb') as f:
        rar.tofile(f)
    print('saved to file in %.3f seconds' % (time() - t_start))

    t_start = time()
    with open('array.bin', 'rb') as f:
        nar = array('d')
        nar.fromfile(f, 10**7)
    print('loaded from file in %.3f seconds' % (time() - t_start))

    t_start = time()
    for i in range(len(nar)):
        if nar[i] != rar[i]:
            print('ne')
            break
    print('compared in %.3f seconds' % (time() - t_start))

    t_start = time()
    eq = nar == rar
    if not eq:
        print('ne')
    print('compared" in %.3f seconds' % (time() - t_start))