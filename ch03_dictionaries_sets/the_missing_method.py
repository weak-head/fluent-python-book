
# It's much better to inherit from
# colletions.UserDict
#
# Converts non-string keys on lookup to string
class StrKeyDict(dict):
    
    def __missing__(self, key):
        if isinstance(key, str):
            raise KeyError
        else:
            return self[str(key)]

    def get(self, key, default=None):
        try:
            return self[key]
        except KeyError:
            return default

    def __contains__(self, key):
        return key in self.keys() or str(key) in self.keys()


def str_key_dict_usage():

    d = StrKeyDict({'2': 'two', '4': 'four'})

    print(d[2])
    print(d['2'])
    try:
        print(d[1])
    except KeyError as ke:
        print(ke)

    print()

    print(d.get('2'))
    print(d.get(4))
    print(d.get(1, 'n/a'))

    print()

    print(2 in d)
    print(1 in d)

    d[7] = 'seven' # this gives number as key, not the string
    print(d[7])

    try:
        print(d['7'])
    except KeyError as ke:
        print('key not found')

    print(d)


str_key_dict_usage()