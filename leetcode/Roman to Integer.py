def romanToInt(s):
    res=0
    decode = {"I": 1, "V" : 5, "X" :10, "L": 50, "C": 100, "D" : 500, "M" : 1000}

    for x in range(len(s)):
        if x +1 < len(s) and decode[s[x]]< decode[s[x+1]]:
            print("X: " + str(x) + " decode: " + str(decode[s[x]])+ " decode: " + str(decode[s[x+1]]))
            res-=decode[s[x]]
        else:
            res+=decode[s[x]]
        print("res " + str(res))
    return res


print(romanToInt("IIIIX"))