
class HashTable :
    def __init__(self,length =10 , probing = 1):
        
        self.length = length
        self.table = [[None,""]  for _ in range(length)]
        self.probing = probing

    def hash_function(self,key,i):
        
        hash = (key + i**self.probing) % self.length
        return hash

    def insert(self,key,value):
        i = 0
        while True :
            
            if i > (self.length - 1) :
                print("HASH TABLE IS FULL !")
                break
                
            hash = self.hash_function(key,i)

            if self.table[hash][0] : i += 1

            else :
                self.table[hash][0] = key
                self.table[hash][1] = value
                break
    
    def display(self):

        for key,value in self.table:
            if key :
                print(f"{key} {value}")

    def print_hash_table(self) : print(self.table)

if __name__ == '__main__':
    table_len,probing = list(map(int,input("ENTER THE LENGTH AND PROBING ON HASH TABLE -> ").rstrip().split()))
    table1 = HashTable(table_len,probing)

    for i in range(3):
        phno,name = input("ENTER THE KEY AND VALUE -> ").rstrip().split()
        phno = int(phno)
        table1.insert(phno,name)

    table1.display()
    
        

    