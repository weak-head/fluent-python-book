#!/bin/python


def ordered_dict():
    '''
    The dictionary that preserves insertion order.
    '''

    import collections

    od = collections.OrderedDict()

    od[1] = 'first'
    od[2] = 'second'
    od[3] = 'third'

    # LIFO
    print('LIFO:')
    print('  ', od.popitem())
    print('  ', od.popitem())

    od[4] = 'forth'
    od[5] = 'fifth'

    # FIFO
    print('FIFO:')
    print('  ', od.popitem(last=False))
    print('  ', od.popitem(last=False))
    print('  ', od.popitem(last=False))

## ---------------------------------------- ##

ordered_dict()