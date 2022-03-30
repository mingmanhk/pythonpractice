"""def romanToInt(s):
    res= 0  
    #decode= { "I": 0, "IV": 4, "V": 5, "IC": 9,"X": 10, "XL": 40, "L": 50, "XC": 90, "C": 100, "CD": 400,"D": 500, "CM": 900, "M": 1000}
    decode = {"I": 1, "V" : 5, "X" :10, "L": 50, "C": 100, "D" : 500, "M" : 1000}
    
    for x in range(len(s)):
        if x+1 < len(s) and decode[s[x]]< decode[s[x+1]]:
            res-=decode[s[x]]
        else:
            res+=decode[s[x]]
    return res

print(romanToInt("MCMXCIV")) 
"""
from audioop import reverse


def intToRoman(nums):
    res =[]
    decode=  [["I", 1],
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

    for i, v in reversed(decode):
        print("---------------"+ i)
        print("nums % a " + str(nums % v))
        print("nums// v " + str(nums// v))
        print("---------------")
        if nums// v:
            res +=(i* (nums //v))
            print("res +=(i* (nums //v)) " + str((i* (nums //v))))
            nums=nums % v
    return ''.join(res)

print(intToRoman(333))
