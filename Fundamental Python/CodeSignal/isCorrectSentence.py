#Link: https://app.codesignal.com/tournaments/q34suwQKwaMczpqia/D

# Original 
def isCorrectSentence(inputString):
    if 'A' <= inputString[0] <= 'Z' and inputString[-1] == '.':
        return True
    return False

# Using built-in func
def isCorrectSentence(inputString):
    if inputString[0].isupper() and inputString[-1] == '.':
        return True
    return False