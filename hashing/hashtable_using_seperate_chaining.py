
import hashing.linkedlist1 as ll

class HashTable :

    def __init__(self,length):
        self.length = length
        self.table = [ ll.LinkedList() for _ in range(self.length)]
        

    def hash_function(self,key):
        hash = key % self.length
        return hash

    def insert(self,key,value): 

        hash = self.hash_function(key)
        
        self.table[hash].insert_at_end(value)
            
    def display(self):
        print("-"*10)
        for i in self.table:
            print(i.display())
        print("-"*10)

    def find(self,key,value):
        if key : 
            hash = self.hash_function(key)
            print(f"{hash} IN HASH TABLE ")
            p = self.table[hash].find_value(value)
            return (hash,p)
        
    def delete(self,key,value):
        if key : 
            hash,p = self.find(key,value)
            self.table[hash].delete_value_at(p)
            

if __name__ == "__main__":

    ht = HashTable(7)

    key,value = input("ENTER KEY AND VALUE --> ").rstrip().split()
    key = int(key)
    ht.insert(4,"mdfd")
    ht.insert(key,value)
    ht.insert(3,"goa")
    ht.insert(4,"hio")
    ht.insert(8,"testi")
    #print("found = ",ht.find(4,"hio"))
    ht.display()
    print(ht.length)

    r,c = ht.find(4,"hio")
    print(r,c)

    ht.delete(4,"fullo")
    ht.display()