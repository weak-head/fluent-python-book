from collections import deque
from itertools   import  islice

def tail_filter():
    """deque could be used as unix-like tail."""

    with open('deque_usecases.py', 'r') as f:
        last_five = zip(range(5), deque(f, 5))
        numbered = ['{:0>2d} {}'.format(n, s) for n, s in last_five]
        print(''.join(numbered))

def moving_average(iterable, n=3):
    it = iter(iterable)

    # first n-1 items of the iterable
    avgr = deque(islice(it, n-1))
    avgr.appendleft(0)
    s = sum(avgr)

    for i in it:
        s -= avgr.popleft()

        avgr.append(i)
        s += i

        yield s / n



if __name__ == '__main__':
    tail_filter()
    print(list(moving_average([10, 20, 30, 40, 50, 60, 70])))