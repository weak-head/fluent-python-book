# fluent-python-book

This repo is a playground that contains a source code related to topics that are discussed in the [Fluent Python](http://shop.oreilly.com/product/0636920032519.do) book.

## Sequences and Collections

* list comprehensions (listcomps)
* generator expressions (genexps)
* bisect.bisect & bisect.insort
* heapq.heappush & heapq.heappop

The way how value is being stored:

* container sequences
    * list
    * tuple
    * collections.namedtuple
    * collections.deque
    * queue.Queue
    * queue.LifoQueue
    * queue.PriorityQueue
    * multiprocessing.JoinableQueue
    * asyncio.Queue
    * asyncio.LifoQueue
    * asyncio.PriorityQueue
    * asyncio.JoinableQueue
* flat sequences
    * str
    * bytes
    * bytearray
    * memoryview
    * array.array

Mutability:

* mutable
    * list
    * bytearray
    * array.array
    * collections.deque
    * memoryview
    * ...
* immutable
    * tuple
    * collections.namedtuple
    * str
    * bytes

## Mapping types (Dictionaries and Sets)

* collections.abc
    * Mapping
    * MutableMapping
* dictionary comprehensions (dictcomp)

Variations:

* dict
* collections.defaultdict
* collections.OrderedDict
* collections.ChainMap
* collections.Counter
* collections.UserDict

Extension:

* `__missing__`
* `__contains__`
* `__getitem__`
* `__setitem__`

Immutable Proxy:

* types.MappingProxyType

