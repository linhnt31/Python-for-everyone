# Link: https://app.codesignal.com/tournaments/XotaK3abwBm2ryMjM/E/solutions

def amendTheSentence(s):
    ans = ''
    tmp = s[0]
    for ind, sub in enumerate(s):
        if ind == 0:
            ans += tmp.lower()
            continue
        if sub.isupper():
            ans = ans + ' '
        ans += sub.lower()
    return ans