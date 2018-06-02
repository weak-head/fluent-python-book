#!/bin/python

# this tuple is immutable and could
# be easily hashed
tuple_tuple = (10, 20, (30, 40))
print('%s -> %s\n' % (tuple_tuple, hash(tuple_tuple)))

# but this one contains mutable list
# and even despite the fact that tuple is
# immutable, we cannot generate hash for it
tuple_list = (10, 20, [30, 40])
try:
    print('%s -> %s\n' % (tuple_list, hash(tuple_list)))
except:
    print('cant generate hash for %s\n' % str(tuple_list))

# but if the list is converted to frozenset
# it works as expected
tuple_frozenset = (10, 20, frozenset([30, 40]))
print('%s -> %s\n' % (tuple_frozenset, hash(tuple_frozenset)))

######################################################################

# here are different ways how we can create dictionaries:

a = dict(one=1, two=2, three=3)
print('a:', a)

b = {'one': 1, 'two': 2, 'three': 3}
print('b:', b)

c = dict(zip(['one', 'two', 'three'], [1, 2, 3]))
print('c:', c)

d = dict([('one', 1), ('two', 2), ('three', 3)])
print('d:', d)

e = dict({'one': 1, 'two': 2, 'three': 3})
print('e:', e)
