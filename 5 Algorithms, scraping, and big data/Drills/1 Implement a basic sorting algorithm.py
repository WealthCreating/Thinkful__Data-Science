'''
Pick an algorithm we haven't covered here (you probably want to pick one of the simpler ones, but it's up to you.
Implement it in Python below and see how it compares in sorting our short and long lists.
You should be able to easily find guides on how to implement any of the algorithms.
'''
import time
import random

# Heap sort

def swap(items, a, b):
    items[a], items[b] = items[b], items[a]

def heapify(items, end, x):
    a = 2 * x + 1
    b = 2 * (x + 1)
    max = x
    if a < end and items[x] < items[a]:
        max = a
    if b < end and items[max] < items[b]:
        max = b
    if max != x:
        swap(items, x, max)
        heapify(items, end, max)

def heap_sort(items):
    end = len(items)
    start = end // 2 - 1
    [heapify(items, end, x) for x in range(start, -1, -1)]
    for x in range(end-1, 0,-1):
        swap(items, x, 0)
        heapify(items, x, 0)

random.seed(a=100)

short_list = list(random.sample(range(1000000), 10))
long_list = list(random.sample(range(1000000), 10000))

t0 = time.time()
heap_sort(short_list)
print('Time for short list: {}'.format(time.time() - t0))

t0 = time.time()
heap_sort(long_list)
print('Time for long list: {}'.format(time.time() - t0))
