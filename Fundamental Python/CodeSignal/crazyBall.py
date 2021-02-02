# Source: https://app.codesignal.com/arcade/python-arcade/itertools-kit/nPt9LX3Piip9ZspLv/solutions

from itertools import combinations

def crazyball(players, k):
    return (list(combinations(sorted(players), k)))
