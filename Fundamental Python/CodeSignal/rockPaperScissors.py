# Source: https://app.codesignal.com/arcade/python-arcade/itertools-kit/d9Ru2ARE5tXoQ9KgR/solutions

from itertools import permutations

def rockPaperScissors(players):
    return sorted(list(permutations(players, 2)))
