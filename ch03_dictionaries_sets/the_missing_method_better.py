#!/bin/python

import collections

# collections.UserDict subclasses MutableMapping
class StrKeyDict(collections.UserDict):

    def __missing__(self, key):
        if isinstance(key, str):
            raise KeyError
        else:
            return self[str(key)]

    def __contains__(self, key):
        return str(key) in self.data

    def __setitem__(self, key, value):
        # collections.UserDict uses internal dictionary
        # more like aggregation than inheritance
        self.data[str(key)] = value

d = StrKeyDict({2: 'two', '3': 'three', 4: 'four'})

print()
print(d)

print()
print(d[2])
print(d['2'])

print()
print(d.get(3))
print(d.get('3'))

print()
print(2 in d)
print('2' in d)
