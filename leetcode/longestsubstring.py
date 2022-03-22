def lengthOfLongestSubstring(text):
    checker = []
    size =0
    # scanning letter
    for x in text:
        print(checker)
        if x in checker:
            print("flag: " + str(len(checker)))
            checker = checker[checker.index(x)+1:]
        checker.append(x)
        size = max((len(checker)), size)
    return size


lengthOfLongestSubstring("abcabcbb")