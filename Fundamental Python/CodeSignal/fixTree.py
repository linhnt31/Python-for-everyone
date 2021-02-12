# Source: https://app.codesignal.com/arcade/python-arcade/drilling-the-lists/qtoFLsK47rS6B5iEN/solutions


# Method 1
def fixTree(tree):
    return [" " * ((len(x) - len(x.strip()))//2) + x.strip() + " " * ((len(x) - len(x.strip()))//2) for x in tree]

# Method 2
def fixTree(tree):
    return [x.strip().center(len(x)) for x in tree]
