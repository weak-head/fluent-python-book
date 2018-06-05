

def naive_dict_get():
    '''
    Naive approach using dict.get(k, default)
    that is better than having KeyError
    whenever key is not found using d[k]
    '''

    import sys
    import re

    WORD_RE = re.compile(r'\w+')

    index = {}

    with open('handling_missing_keys.py', encoding='utf-8') as fp:
        for line_no, line in enumerate(fp, 1):
            for match in WORD_RE.finditer(line):
                word = match.group()
                column_no = match.start() + 1
                location = (line_no, column_no)

                occurrences = index.get(word, [])
                occurrences.append(location)
                index[word] = occurrences

    for word in sorted(index, key=str.upper):
        print(word, len(index[word]), index[word])


if __name__ == '__main__':
    naive_dict_get()