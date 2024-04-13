
length_of_hash_table = 7

def hash_function(key,i):
    hash = (key + i) % length_of_hash_table
    return hash

def entry_in_hash_table(key,value):
    i = 0
    while True :
        
        if i > (length_of_hash_table - 1) :
            print("HASH TABLE IS FULL !")
            break
            
        hash = hash_function(key,i)

        if hash_table[hash] :
            i += 1

        else :
            hash_table[hash] = value
            break


hash_table = [ 0 for _ in range(length_of_hash_table - 1 )]

if __name__ == '__main__':
 
    for i in range(3):
         key,value = list(map(int,input("ENTER THE KEY AND VALUE -> ").rstrip().split()))
         entry_in_hash_table(key,value)
    
    print(f"HASH TABLE = {hash_table}")
        

    