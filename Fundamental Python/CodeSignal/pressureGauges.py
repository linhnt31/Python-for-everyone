# Source: https://app.codesignal.com/arcade/python-arcade/drilling-the-lists/SkTfc263CQbGNMtoj/solutions

# Method 1: 
def pressureGauges(morning, evening):
    return [list(map(lambda x, y: min(x, y), morning, evening)), list(map(lambda x, y: max(x, y), morning, evening))]

# Method 2: 
def pressureGauges(morning, evening):
    return list(zip(*[(min(t),max(t)) for t in zip(morning, evening)]))
