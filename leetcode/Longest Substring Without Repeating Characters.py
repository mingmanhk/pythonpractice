def lengthOfLongestSubstring(s):
    str_list = []
    max_length = 0
    runtime = 0
    
    for x in s:
        #print("runtime: " + str(runtime))
        print("checking: " + x)
        
        if x in str_list:
            print(x + " matched : " + str(str_list[str_list.index(x)+1:])) 
            str_list = str_list[str_list.index(x)+1:]
    
        str_list.append(x)    
        max_length = max(max_length, len(str_list))
        #print("str_list: " + str(str_list)) print("max_length: " + str(max_length)) 
        #print("len(str_list): " + str(len(str_list)))   
    return max_length

print(lengthOfLongestSubstring("abcbbccd"))