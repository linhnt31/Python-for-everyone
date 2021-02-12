""" *strip() and center(width, fillchar)*
- strip(): returns 'a copy of the string' with both *leading* and *trailing* characters removed (based on the string argument passed).

- center():  returns a string which is padded with the specified character.

- EXERCISES: 
    + ./CodeSignal/fixTree.py
"""

string = '      linhnt 99  ntlinhhp' 
# default: remove leading and trailing whitespaces.
print(string.strip())  # Output: 'linhnt 1999'
print(string.strip('9')) # Output: '      linhnt    '

# String whose set of characters are to be removed from original string at both its ends.
print(string.strip().strip('lhnti')) # Output: '99  ntlinhhp'


str1 = "linhnt"
str2 = '*    '
print(str2.strip().center(len(str2)))
print(str1.center(20, '*'))
