#!/bin/python

from types import MappingProxyType

d = {1: 'one', 2: 'two'}
immutable_d = MappingProxyType(d)

print('d:', d)
print('im:', immutable_d)

print(immutable_d[1])

try:
    immutable_d[3] = 'three'
except:
    print("doesn't support item assignment")

d[3] = 'three'

print('d:', d)
print('im:', immutable_d)