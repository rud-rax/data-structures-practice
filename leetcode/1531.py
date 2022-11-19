

def compress(text) :
    
    c = 0 
    
    i = 0 
    j =0 
    while j < len(text) :
        if text[i] == text[j] :
            c+=1
        else :
            if c > 1 : 
                text = text[:i+1] + str(c) + text[j:]
                
                j = i + 2
                
            i = j
            j -=1
            c = 0 
                 
        j+=1
     
    if c > 1 :    
        text = text[:i+1] + str(c) 

    return text

def compressList(text) :
    c = 0 
    ans = ""
    i = 0 
    j =0 
    while j < len(text) :
        if text[i] == text[j] :
            c+=1
        else :
            ans += text[i]
            if c > 1 : 
                # text = text[:i+1] + str(c) + text[j:]
                ans += str(c)
                
                j = i + 2
                
            i = j
            j -=1
            c = 0 
                 
        j+=1
     
    ans += text[i]
    if c > 1 :    
        ans+= str(c) 

    return ans
    

if __name__ == "__main__" :
    # txt = 'aaabbxxxacgcdddde'
    
    txt = ["a","a","b","b","c","c","c"]
    txt = ["a","b","b","b","b","b","b","b","b","b","b","b","b"]
    # txt = ["a"]
    # txt = 'aaabcccdddd'
    
    print(compressList(txt))
    