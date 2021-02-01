# Source: https://app.codesignal.com/arcade/python-arcade/caravan-of-collections/aarR4B273h5D2x8ry

from collections import deque

def doodledPassword(digits):
    n = len(digits)
    res = [deque(digits) for _ in range(n)]
    deque(map(lambda x: x[1].rotate(-x[0]), enumerate(res)), 0)
    return [list(d) for d in res]
