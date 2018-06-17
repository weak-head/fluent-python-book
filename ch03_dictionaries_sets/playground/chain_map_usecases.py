#!/bin/python

from collections import ChainMap
from argparse    import ArgumentParser
from os          import environ

def get_default_config():
    return { 'APP_PORT': 2332
           , 'APP_TIMEOUT': 60 
           , 'APP_WORKERS': 4
           }

def create_argparser():
    parser = ArgumentParser()
    
    parser.add_argument('-p', dest='APP_PORT')
    parser.add_argument('-t', dest='APP_TIMEOUT')
    parser.add_argument('-n', dest='APP_WORKERS')

    return parser

if __name__ == '__main__':
    parser = create_argparser()

    args = parser.parse_args()

    explicit_args = {k: v for k, v in vars(args).items() if v}
    default_val   = get_default_config()

    print('\nargs:')
    for k, v in explicit_args.items():
        print(k, ' -> ', v)

    print('\nsys env:')
    for k, v in sorted(environ.items(), key=lambda x: x[0]):
       print(k, ' -> ', v)

    app_config = ChainMap(explicit_args, environ, default_val)

    print('\n\napp vales:')
    print('APP_PORT', ' -> ', app_config['APP_PORT'])
    print('APP_TIMEOUT', ' -> ', app_config['APP_TIMEOUT'])
    print('APP_WORKERS', ' -> ', app_config['APP_WORKERS'])