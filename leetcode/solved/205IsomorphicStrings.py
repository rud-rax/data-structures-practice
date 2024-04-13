
def solve(s , t):
    
    if len(s) != len(t):
        return False
    
    letdic = {}
    for i in range(len(s)) :
        
        letdic[s[i]] = t[i]
        letdic[t[i]] = s[i]
        
    print(letdic)
    
    for i in range(len(s)) :
        if letdic[s[i]] != t[i]:
            return False
        
    for i in range(len(t)) :
        if letdic[t[i]] != s[i] :
            return False
        
    return True
      
def solve1(s , t) :
    
    if len(s) != len(t):
        return False
    
    ss = []
    tt = []
    for i in range(len(s)) :
        
    
        
    

if __name__ == "__main__" :
    # print(solve(s = "egg", t = "add"))
    # print(solve(s = "foo", t = "bar"))
    print(solve(s = "paper", t = "title"))
    
    