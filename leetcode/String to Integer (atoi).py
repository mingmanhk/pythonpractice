def myAtoi(teststring):
    #size limit, If the integer is out of the 32-bit signed integer range [-231, 231 - 1], then clamp the integer so that it remains in the range. 
    max_int = 2 ** 31-1
    min_int = -2 ** 31


    i =0
    res = 0;
    checker =set("1234567890")
    isNegative =1
    for i in teststring:
        # check whitespace  
        if i==" ":
            print("whitespace")
        elif i=="-":
        # check +/-
            isNegative=-1
            print("negative")
        elif i=="+":
            print("positive")
        elif i in checker:
            print("checknumber"+ str(i))
            res = res * 10 + int(i)
            print("string:" +i)
    
    #check max and min
    print("check max/min"+ str(i))
    res= res * isNegative
    if res<0:
        return max(res, min_int)
    return min(res, max_int)


print(myAtoi("words and 987"))