# Source: https://app.codesignal.com/arcade/python-arcade/caravan-of-collections/3q55u2MWA2Rw5HvmM/solutions

# Method 1
def transposeDictionary(scriptByExtension):
    return [[v, k] for k, v in sorted(scriptByExtension.items(), key= lambda item: item[1])]

# Method 2
def transposeDictionary(scriptByExtension):
    return sorted([v, k] for k, v in scriptByExtension.items())