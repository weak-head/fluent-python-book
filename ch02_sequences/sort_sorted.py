#!/python/bin

def sorted_convention():
    '''
    list.sort() and sorted() are having a little bit
    different behavior.
    list.sort() modifies the original list.
    sorted() returns a new sorted collection.
    '''

    # both `list.sort()` and `sorted()` accepts optional
    # arguments:
    #   - reverse
    #   - key

    cities = ['San-Francisco', 'Boston', 'Los Angeles', 'Vegas']

    res = sorted(cities)
    print(cities)  # the original collection is not changed
    print(res)     # but this one is sorted

    res = sorted(cities, key=len)
    print(res)

    res = sorted(cities, key=len, reverse=True)
    print(res)


    print(cities)

    cities.sort()
    print(cities)

    cities.sort(key=len)
    print(cities)

    cities.sort(key=len, reverse=True)
    print(cities)


if __name__ == '__main__':
    sorted_convention()