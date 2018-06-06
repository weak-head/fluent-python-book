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

def counter_dict():
    '''
    Counter accumulates number of occurrences.
    '''

    import collections

    cnt = collections.Counter('a lazy dog jumped over the quick fox'.replace(' ', ''))
    print(cnt)

    cnt.update('the dog is not so lazy'.replace(' ', ''))
    print(cnt)

    # 3 most common letters
    print(cnt.most_common(3))

## ---------------------------------------- ##

ordered_dict()
counter_dict()