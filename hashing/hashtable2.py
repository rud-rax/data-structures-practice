
class HashTable :

    def __init__(self,length = 10 , probing = 1):
        
        self.length = length
        self.table = [[None,None]  for _ in range(length)]
        self.probing = probing

    def hash_function(self,key,i):
        
        hash = (key + i**self.probing) % self.length
        return hash

    def insert(self,key,value):

        i = 0
        
        copy_exist = False 
        for phno,_ in self.table :
            if key == phno :
                copy_exist = True
                print("DUPLICATE PHONE NUMBER FOUND ! CANNOT BE INSERTED IN HASH TABLE.")
                break

        while True and not copy_exist :
            
            if i > (self.length - 1) :
                print("HASH TABLE IS FULL !")
                break
                
            hash = self.hash_function(key,i)

            if self.table[hash][0] : i += 1

            else :
                self.table[hash][0] = key
                self.table[hash][1] = value
                break
    

    def find(self,key):
        i = 0
        hash = self.hash_function(key,i)
        while self.table[hash][0] != key :
            
            i +=1
            if i > (self.length - 1) : 
                print("VALUE NOT FOUND")
                break
            
            hash = self.hash_function(key,i)

        else :
            print(f"PHONE NUMBER = {self.table[hash][0]} NAME = {self.table[hash][1]}")
            return hash
            

    def display(self):

        for key,value in self.table:
            if key :
                print(f"{key} {value}")

    def print_hash_table(self) : print(self.table)

if __name__ == '__main__':

    table_len,probing = list(map(int,input("ENTER THE LENGTH AND PROBING OF HASH TABLE -> ").rstrip().split()))
    table1 = HashTable(table_len,probing)

    while True :

        print('''
        ----MENU----
        1 : INSERT
        2 : FIND
        3 : DISPLAY
        0 : EXIT 
         ''')
        operation = int(input("ENTER THE OPERATION YOU WANT TO PERFORM ON HASH TABLE -> "))

        if operation == 1 :
            phno,name = input("ENTER THE PHONE NUMBER AND NAME -> ").rstrip().split()
            phno = int(phno)
            table1.insert(phno,name)
            table1.display()

        if operation == 2 :
            phno = int(input("ENTER THE PHONE NUMBER TO FIND -> "))
            hash = table1.find(phno)
            print(table1.table[hash][1])
        
        if operation == 3 :
            table1.display()
            table1.print_hash_table()
    
        if operation == 0 : 
            break

    