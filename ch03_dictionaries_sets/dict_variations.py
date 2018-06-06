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

def chain_map_dict():
    '''
    chain map allows us to combine multiples
    sources of search into one ordered chain
    '''

    import collections

    local_host = {'alex': True, 'john': False}
    local_domain_controller = {'mike': False, 'alex': True}
    global_domain_controller = {'rob': True}


    cm = collections.ChainMap(local_host, local_domain_controller, global_domain_controller)

    print('alex', cm['alex'])
    print('mike', cm['mike'])
    print('rob', cm['rob'])

    try:
        print('missing', cm['missing'])
    except KeyError as ke:
        print('key not found...')
        print('KeyError:', ke)

## ---------------------------------------- ##

ordered_dict()
counter_dict()
chain_map_dict()