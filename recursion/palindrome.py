
S = "abbaabba"
# S = "aba"
S = "dflsjf"
S = "secies"

def checkPalindrome(s) :
    if not s :
        return True 

    if s[0] == s[-1] :
        return checkPalindrome(s[1:-1])
    return False


def checkPalindrome2(s) :
    if not s :
        return True
    
    return s[0] == s[-1] and checkPalindrome2(s[1:-1])

def checkPalindrome3(s , start , end ) :
    if end <= start :
        return True
    return s[start] == s[end] and checkPalindrome3(s , start+1 , end-1)



if __name__ == "__main__" : 
    # print(checkPalindrome2(S)) 
    # print(checkPalindrome(S)) 
    print(checkPalindrome3(S , 0 , len(S) - 1))


