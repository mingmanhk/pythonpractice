def longestPalindrome(s):
    maxlen = 0
    output =""
    for i in range(len(s)):
        for j in range(i+1, len(s)+1):
            cand = s[i:j]

            if cand == cand[::-1] and len(cand)>maxlen:
                output =cand
                maxlen=len(cand)
    return output