def reverseWords(s: str) -> str:
    a = s.split()
    res= []
    for i in range(len(a)):
        res.append(a[i][::-1])
        
    return " ".join(res)


print(reverseWords("Let's take LeetCode contest"))