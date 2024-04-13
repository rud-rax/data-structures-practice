
class Node :
    def __init__(self,data,nxtptr = None):
        self.data = data
        self.next = nxtptr
        
class LinkedList:
    def __init__(self):
        self.head = None
        self.tail = None
        
    def insert(self,data):
        node = Node(data)
        if not self.head :
            self.head = node
        else :
            self.tail.next = node    
        self.tail = node
        
    def search(self,name):
        itr = self.head
        data_exist = False
        while itr :
            if itr.data[0] == name:
                
                return itr.data[1]
            itr.next
        print("Not Found")
    
class HashTable:
    def __init__(self,length =  97*3):
        self.length = length
        self.table = [None for _ in range(self.length)]
        
    def hash_function(self,name):
        return ((ord(name[0])+ord(name[1])+ord(name[2]) - 97*3))
    
    def insert(self,name,ph):
        if len(name) < 3:
            print("Enter a longer name.")

        data = [name,ph]
        hash = self.hash_function(name)
        if not self.table[hash]:self.table[hash] = LinkedList()
        self.table[hash].insert(data)
    
    def search(self,name):
        hash = self.hash_function(name)
        if self.table[hash] :
            ph = self.table[hash].search(name)
            if ph:
                print(f"NAME : {name} \nNUMBER : {ph}")
        else : 
            print("Not Found")
        
if __name__ == '__main__':
    n = int(input("NUMBER OF ENTRIES -->"))
    ht = HashTable()
    for _ in range(n):
        name,ph =input("NAME AND NUMBER --> ").rstrip().split()
        ht.insert(name,ph)
        
    for _ in range(n):
        name = input("NAME --> ").rstrip()
        ht.search(name)
        
