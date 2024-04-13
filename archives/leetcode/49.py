from collections import defaultdict



def groupAnagrams(strs) :
        
        hashes = []
        grouped_words = []

        for word in strs :
            d = defaultdict(lambda : 0)
            
            for letter in word :
                d[letter] += 1


            print(d)

            ##
                
                
            
            
                
            
            # hashes.append(d)

def hash_check(word1 , word2) :
    
    if len(word1) != len(word2) : 
        return False
     
    d1 = defaultdict(lambda : 0)
    d2 = defaultdict(lambda : 0)

        
    for letter in word1 :
        d1[letter] += 1

    for letter in word2 :
        d2[letter] += 1

    print(d1 , d2)

    for letter in word1 :
         
        
     

print(hash_check('eat' , 'tea'))
# print(groupAnagrams(["eat","tea","tan","ate","nat","bat"]))
