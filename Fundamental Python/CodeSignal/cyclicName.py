# Source: https://app.codesignal.com/arcade/python-arcade/itertools-kit/QAFXsBY35wRnHkruC

from itertools import cycle

def cyclicName(name, n):
    gen = cycle(name)
    res = [next(gen) for _ in range(n)]
    return ''.join(res)
