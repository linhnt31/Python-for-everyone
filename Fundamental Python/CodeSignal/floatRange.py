# Source: https://app.codesignal.com/arcade/python-arcade/itertools-kit/cDuMQ6Fd4N58zdCWN/solutions

from itertools import count, takewhile

def floatRange(start, stop, step):
    gen = takewhile(lambda x: x < stop ,[start + step*i for i in range(int((stop-start)//step)+1)])
    # Alternative:          gen = takewhile(lambda x: x < stop ,count(start, step))
    return list(gen)
