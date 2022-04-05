def reverseWords(s: str):
    res=[]
    a=s.split()

    for i in reversed(range(len(a))):
        res.append(a[i])
    return " ".join(res)

print(reverseWords("the sky is blue"))