# Source: https://app.codesignal.com/arcade/python-arcade/drilling-the-lists/Enwr8TBeTbuFbuPzu/solutions

from itertools import accumulate

# Time complexity: O(n)
def prefSum(a):
    return list(accumulate(a, lambda x, y: x + y))