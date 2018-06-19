from collections import deque

def tail_filter():
    """deque could be used as unix-like tail."""

    with open('deque_usecases.py', 'r') as f:
        last_five = zip(range(5), deque(f, 5))
        numbered = ['{:0>2d} {}'.format(n, s) for n, s in last_five]
        print(''.join(numbered))


if __name__ == '__main__':
    tail_filter()