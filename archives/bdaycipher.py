

s = 'dzxdestyrwzdedzxdestyrqzfyo'

# words = s.split()
# k = 1 
# for k in range(1 , 27) :
#     for w in words :
#         for l in w : 
#             print(f"{chr(ord(l) + k)}", end = "")

#         print(" " , end = "")
#     print()

                
                
def decoded(s):
    for i in range(1,95):
        string = ""
        for char in s:
            
            if char == " " :
                string += " "
         
            if(ord(char) + i > 126) :
                charc = (ord(char) + i) - 94
                string =  string + chr(charc)
                
            else:
               charc = ord(char) + i
               string =  string + chr(charc) 

        print(string)
        
decoded(s)