def intToRoman(num):
    res=[]
    decode = [["I", 1],
    ["IV", 4],
    ["V", 5],
    ["IX", 9],
    ["X", 10],
    ["XL", 40],
    ["L", 50],
    ["XC", 90],
    ["C", 100],
    ["CD", 400],
    ["D", 500],
    ["CM", 900],
    ["M", 1000]]
    for i, a in reversed(decode):
        print(i, a)
        if num // a:
            res += (i * (num // a))
            num = num % a
    return ''.join(res)

print(intToRoman(3423))

