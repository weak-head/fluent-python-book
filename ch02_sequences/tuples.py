#!/bin/python

from collections import namedtuple

def tuple_unpacking():
    '''
    Pretty straightforward examples of tuple unpacking.
    '''

    name, last_name, age = ('John', 'Doe', 37)
    print(name, last_name, age)

    people = [('Alice', 17),
              ('Bob', 27),
              ('Mallory', 22)]

    for person in sorted(people, key=lambda x: x[1]):
        print('%s (%s)' % person)

    # tuple unpacking could be utilized
    # for swapping values:
    name, last_name = last_name, name

    # another usage it when we are calling a method
    data = (20, 8)
    quotient, remainder = divmod(*data)
    print(quotient, remainder)

    # '_' is simple just same variable as 'filename'
    # an opposite to wildcard syntax in haskell
    import os
    _, filename = os.path.split('/home/user_name/.ssh/idrsa.pub')  # path, last_part
    print(filename)

    # using * allows us to grab excess items
    a, b, *rest = range(5)
    print(a, b, rest)

    a, b, *rest = range(3)
    print(a, b, rest)

    a, b, *rest = range(2)
    print(a, b, rest)

    a, *body, b, c = range(5)
    print(a, body, b, c)

    *head, a, b = range(5)
    print(head, a, b)

    # we can do nested tuple unpacking
    metro_areas = [
        ('Tokyo', 'JP', 36.933, (35.689722, 139.691667)),
        ('Delhi NCR', 'IN', 21.935, (28.613889, 77.293272)),
        ('Mexico City', 'MX', 20.142, (19.433333, -99.134234)),
        ('New York-Newark', 'US', 20.104, (40.808692, -74.029342)),
        ('Sao Paulo', 'BR', 19.692, (-23.34252, -46.462952)),
    ]

    print('{:15} | {:^9} | {:^9}'.format('', 'lat.', 'long.'))
    fmt = '{:15} | {:9.4f} | {:9.4f}'

    for name, cc, pop, (latitude, longitude) in metro_areas:
        if longitude <= 0:
            print(fmt.format(name, latitude, longitude))


def named_tuples():
    '''
    Named tuples are very usefull and easy to use.
    '''

    # two ways to specify field names for named tuple:
    #   - string with names
    #   - enumerable of strings
    City = namedtuple('City', 'name country population coordinates')
    Coordinates = namedtuple('Coordinates', 'latitude longitude')

    tokyo = City('Tokyo', 'JP', 36.933, Coordinates(35.689722, 139.691667))

    print(tokyo)
    print(tokyo.name)
    print(tokyo.country)
    print(tokyo.population)
    print(tokyo.coordinates)
    print(tokyo.coordinates.latitude)
    print(tokyo.coordinates.longitude)

    print(tokyo[1])

    # a few special methods are very handy:
    #  - _make
    #  - _asdict
    #  - _fields

    delhi_data = ('Delhi NCR', 'IN', 21.9, Coordinates(28.613242, 77.2083242))

    print(City._fields)
    delhi = City._make(delhi_data)
    print(delhi)

    print(delhi._asdict())
    for key, value in delhi._asdict().items():
        print(key, ': ', value)


if __name__ == '__main__':
    tuple_unpacking()

    named_tuples()