# Source: https://app.codesignal.com/arcade/python-arcade/itertools-kit/k2MEPqLJn5YEWafkt/solutions

from itertools import product

def crackingPassword(digits, k, d):
    def createNumber(digs):
        return "".join(map(str, digs))

    return sorted([createNumber(x) for x in list(product(digits, repeat=k)) if int(createNumber(x)) % d == 0])
