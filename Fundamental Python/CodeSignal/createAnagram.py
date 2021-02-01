# Link: https://app.codesignal.com/tournaments/ppN7aDqauR4sag8bE/B

def createAnagram(s, t):

    cnt1 = [0] * 26
    cnt2 = [0] * 26
    for i in range(len(s)):
        cnt1[ord(s[i]) - ord('A')] += 1
        cnt2[ord(t[i]) - ord('A')] += 1

    ans = 0
    for i in range(26):
        ans += abs(cnt1[i]-cnt2[i])

    return ans / 2