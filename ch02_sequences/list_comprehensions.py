#!/bin/python


def readability_example():

    # using simple for loop
    symbols = '$%^&*('
    codes = []
    for symbol in symbols:
        codes.append(ord(symbol))
    print(codes)

    # using list comprehension
    symbols = '$%^&*('
    codes = [ord(symbol) for symbol in symbols]
    print(codes)


def map_filter_example():

    # why do map and filter are so ugly in python?
    # haskell, where are you?
    #   filter (>127) . map ord $ "$%&*("
    symbols = '$%^&*('
    codes = list(filter(lambda c: c > 127, map(ord, symbols)))
    print(codes)

    # comprehansions are bearable
    # and are similar to haskell:
    #  [ord x | x <- "$%^&*(", ord x > 127]
    symbols = '$%^&*('
    codes = [ord(x) for x in symbols if ord(x) > 127]
    print(codes)


def cartesian_product_example():

    sizes = ['S', 'M', 'L', 'XL']
    colors = ['black', 'pink', 'yellow']

    # naive approach
    tshirts = []
    for size in sizes:
        for color in colors:
            tshirts.append((size, color))
    print(tshirts)

    # comprehension
    tshirts = [(size, color) for size in sizes
                             for color in colors]
    print(tshirts)


def genexps_example():
    '''
    genexps save memory because they are kind of lazy
    and yeild items on demand one-by-one, using the iterator
    protocol instead of building the whole list as listcomps do.
    '''

    symbols = '$%&*('
    codes = tuple(ord(symbol) for symbol in symbols)
    print(codes)

    import array
    ar = array.array('I', (ord(symbol) for symbol in symbols))
    print(ar)

    colors = ['black', 'red', 'green']
    sizes = ['S', 'M', 'XL']
    for tshirt in ("%s %s" % (size, color) for size in sizes
                                           for color in colors):
        print(tshirt)


if __name__ == '__main__':
    cartesian_product_example()

    readability_example()

    map_filter_example()

    genexps_example()