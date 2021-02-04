# Source: 

# Method 1:
def swap(lst):
    for i in range(0, len(lst), 2):
        lst[i], lst[i+1] = lst[i+1], lst[i]
    return lst
def correctLineup(athletes):
    return swap(athletes)

# Method 2:
def correctLineup(athletes):
    return [athletes[i^1] for i in range(len(athletes))]
