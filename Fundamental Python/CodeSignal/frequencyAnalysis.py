# Source: https://app.codesignal.com/arcade/python-arcade/caravan-of-collections/pE4t3DcoTRfwHwYG8/solutions

from collections import Counter

def frequencyAnalysis(encryptedText):
    return Counter(encryptedText).most_common(1)[0][0]
