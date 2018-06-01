#!/bin/python

from collections import deque

def deque_example():

    dq = deque(range(10), maxlen=10)
    print('dq:')
    print(dq)
    print()

    dq.append(55)
    print('append 55')
    print(dq)
    print()

    dq.appendleft(-55)
    print('appendleft -55')
    print(dq)
    print()

    dq.rotate(3)
    print('rotate 3')
    print(dq)
    print()

    dq.rotate(-6)
    print('rotate -6')
    print(dq)
    print()

    dq.extend([77, 88, 99])
    print('extend 77 88 99')
    print(dq)
    print()

    dq.extendleft([-77, -88, -99])
    print('extendleft -77 -88 -99')
    print(dq)
    print()

if __name__ == '__main__':
    deque_example()

    # related queues:
    #  - queue.Queue
    #  - multiprocessing.Queue
    #  - multiprocessing.JoinableQueue
    #  - asyncio.Queue
    #  - asyncio.LifoQueue
    #  - asyncio.PriorityQueue
    #  - asyncio.JoinableQueue
    #  - heapq -> lists .heappop .heappush