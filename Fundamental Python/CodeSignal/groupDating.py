# Source: https://app.codesignal.com/arcade/python-arcade/drilling-the-lists/okcMELPg5HbvSKodi/solutions

def groupDating(male, female):
    return [[x for x, y in list(zip(male, female)) if x != y]] + [[y for x, y in list(zip(male, female)) if x != y]]
