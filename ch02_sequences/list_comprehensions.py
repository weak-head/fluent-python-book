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