# Source: https://app.codesignal.com/arcade/python-arcade/itertools-kit/opua5BqfJSaW9ny4Q/solutions

from itertools import permutations

# Method 1
def kthPermutation(numbers, k):
    return list(list(permutations(numbers, len(numbers)))[k-1])

# Method 2
def kthPermutation(numbers, k):
    # start = 1 and stop = None --> get value at (k-1)th
    return next(islice(permutations(numbers), k-1, None))